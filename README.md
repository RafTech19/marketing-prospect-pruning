# 📊 Marketing Performance Optimization through Prospect Pruning

**Final Project — Comprehensive Data Analytics Bootcamp (CODA RMT 015 · Group 3)**

A data-driven marketing analysis that identifies and eliminates low-performing 
prospect segments to improve conversion efficiency and reduce acquisition costs.

---

## 🚀 Business Impact

| Metric | Before | After (10% Pruning) |
|---|---|---|
| Conversion Rate | 87.65% | **90.53%** (+2.88%) |
| Total AdSpend | $40M | **$31.8M** (~20% saved) |
| Prospects Pruned | — | 1,632 (low-intent segments) |
| Savings per Lost Conv | — | **$6,557** |

---

## 🔍 Key Findings

- **Previous Purchases** is the strongest pruning signal — eliminating 
  prospects with 0 transactions yields the highest CR uplift with minimal volume loss
- **Demographics alone** (age, gender, income) showed no significant 
  variance in CR (>85% across all segments) — not reliable for segmentation
- **Referral & PPC** channels lead conversion performance (88.31% & 88.28%)
- High-intent audience profile: **3–4 previous purchases + 8–9 email opens → CR >92%**

---

## 🛠️ Tech Stack

`Pandas` · `PySpark` · `PostgreSQL (NeonDB)` · `Apache Airflow` · 
`Great Expectations` · `Looker Studio` · `SQLAlchemy`

---

## 🏗️ Data Pipeline
Kaggle API → PySpark (ETL) → NeonDB/PostgreSQL → Airflow (daily schedule) → Looker Studio

**Star Schema:** `dim_customer` · `dim_channel` · `dim_campaign_type` · `fact_marketing_performance`

**Data Validation (Great Expectations):** Unique CustomerID, valid campaign channels, 
correct data types, Conversion column integrity

---

---

## 👥 Team

| Name | Role |
|---|---|
| Zafirah Aida Adista | Data Analyst |
| Muhammad Rafli Febriyanto | Data Analyst |
| Muhamad Imam Ferdiansyah | Data Engineer |
