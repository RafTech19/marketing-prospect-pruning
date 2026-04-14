import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator


default_args = {
    'owner': 'imam',
    'start_date': dt.datetime(2024, 11, 8),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=600),
}


with DAG('final_project_dag',
         default_args=default_args,
         schedule_interval='10,20,30 9 * * 6',
         catchup=False,
         ) as dag:

    python_final_project = BashOperator(task_id='python_final_project', bash_command='sudo -u airflow python /opt/airflow/scripts/final_project.py')

    

python_final_project