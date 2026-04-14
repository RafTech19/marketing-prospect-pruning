from importlib.resources import path

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, monotonically_increasing_id

# ======================================================
# 1. INISIALISASI SPARK DENGAN JDBC DRIVER
# ======================================================
spark = SparkSession.builder \
    .appName("DigitalMarketing_Final_Project_Group3") \
    .config("spark.jars.packages", "org.postgresql:postgresql:42.7.2") \
    .getOrCreate()

# ======================================================
# 2. EXTRACT (Membaca Dataset)
# ======================================================
# Pastikan file CSV ini ada di folder yang sama dengan notebook Anda
import kagglehub
import os
import pandas as pd
print("KaggleHub version:", kagglehub.__version__)

DATASET_ROOT_DIR = "/opt/airflow/data/"


path = kagglehub.dataset_download("rabieelkharoua/predict-conversion-in-digital-marketing-dataset")
print("Path to dataset files:", path)
if not os.path.exists(DATASET_ROOT_DIR):
    os.makedirs(DATASET_ROOT_DIR)
os.system("cp -r {}/* {}".format(path, DATASET_ROOT_DIR))
print("Path to dataset files:", path)
df_raw= spark.read.csv('/opt/airflow/data/digital_marketing_campaign_dataset.csv', header=True, inferSchema=True)

# ======================================================
# 3. TRANSFORM (Logika sesuai final_project.py)
# ======================================================

# A. Drop kolom tidak relevan & Ubah Tipe Data
# 2. Transformasi: Cast Tipe Data, Rename Kolom, dan Drop Kolom Sekaligus
df_final = df_raw.withColumn("PagesPerVisit", col("PagesPerVisit").cast("int")) \
                 .withColumn("CustomerID", col("CustomerID").cast("string")) \
                 .withColumn("Conversion", col("Conversion").cast("boolean")) \
                 .withColumnRenamed("ConversionRate", "HistoryCR") \
                 .drop("AdvertisingPlatform", "AdvertisingTool")

# 3. Simpan Data ke CSV
output_csv_path = '/opt/airflow/data/transform_result_digital_marketing_campaign_pipeline.csv'

# Mengonversi ke Pandas hanya untuk menyimpan (cocok untuk data skala kecil/menengah)
df_final.toPandas().to_csv(output_csv_path, index=False)

# ======================================================
# 4. DATA MODELING (STAR SCHEMA) - DEFINISI VARIABEL
# ======================================================

# 1. Membuat dim_customers
dim_customer = df_final.select(
    col("CustomerID").alias("customer_id"),
    col("Age").alias("age"),
    col("Gender").alias("gender"),
    col("Income").alias("income")
).distinct()

# 2. Membuat dim_campaign_type
dim_campaign_type = df_final.select(
    col("CampaignType").alias("campaign_type_name")
).distinct().withColumn("campaign_type_id", monotonically_increasing_id())

# 3. Membuat dim_channel (PASTIKAN ALIAS KOLOM DI SINI)
dim_channel = df_final.select(
    col("CampaignChannel").alias("campaign_channel")
).distinct().withColumn("channel_id", monotonically_increasing_id())

# 4. Membuat fact_marketing_performance (Termasuk metrik tambahan)
fact_marketing = df_final.alias("raw").join(
    dim_customer, 
    col("raw.CustomerID") == col("customer_id"), 
    "inner"
).join(
    dim_channel.alias("chan"), 
    col("raw.CampaignChannel") == col("chan.campaign_channel"), 
    "inner"
).select(
    monotonically_increasing_id().alias("performance_id"),
    col("customer_id"),
    col("chan.channel_id"),
    col("raw.AdSpend").alias("ad_spend"),
    col("raw.ClickThroughRate").alias("click_through_rate"),
    col("raw.HistoryCR").alias("conversion_rate"), 
    # -----------------------------------------------------------
    col("raw.WebsiteVisits").alias("website_visits"),
    col("raw.PagesPerVisit").alias("pages_per_visit"),
    col("raw.TimeOnSite").alias("time_on_site"),
    col("raw.SocialShares").alias("social_shares"),
    col("raw.EmailOpens").alias("email_opens"),
    col("raw.EmailClicks").alias("email_clicks"),
    col("raw.PreviousPurchases").alias("previous_purchases"),
    col("raw.LoyaltyPoints").alias("loyalty_points"),           
    col("raw.Conversion").alias("conversion")
)

# ======================================================
# 5. LOAD KE NEON DB
# ======================================================

jdbc_url = "jdbc:postgresql://ep-soft-dawn-ai95tj05-pooler.c-4.us-east-1.aws.neon.tech/final_project_group3"

connection_properties = {
    "user": "neondb_owner",
    "password": "npg_KYMgl7bj2BOC",
    "driver": "org.postgresql.Driver",
    "ssl": "true",
    "sslmode": "require"
}

def upload_table(df, table_name):
    try:
        print(f"Sedang mengupload tabel: {table_name}...")
        df.write.jdbc(url=jdbc_url, table=table_name, mode="overwrite", properties=connection_properties)
        print(f"Berhasil mengupload {table_name}")
    except Exception as e:
        print(f"Gagal mengupload {table_name}. Error: {str(e)}")

# EKSEKUSI UPLOAD (Sekarang variabel sudah didefinisikan di atas)
upload_table(dim_customer, "dim_customer")
upload_table(dim_channel, "dim_channel")
upload_table(dim_campaign_type, "dim_campaign_type")
upload_table(fact_marketing, "fact_marketing")

print("\n--- SELURUH PROSES ETL SELESAI ---")