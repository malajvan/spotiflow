import datetime as dt
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.base_hook import BaseHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.postgres.operators.postgres import PostgresOperator
from sqlalchemy import create_engine
from airflow.utils.dates import days_ago

from extract import extract
from load import load

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': dt.datetime(2023,1,29),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1)
}

dag = DAG(
    'spotify_dag',
    default_args=default_args,
    description='Spotify ETL process 1-min',
    schedule_interval=dt.timedelta(minutes=50),
)

def ETL():
    print("Starts flow")
    load(extract)
    print('finished flow')

with dag:    

    run_etl = PythonOperator(
        task_id='spotify_dag',
        python_callable=ETL,
        dag=dag,
    )

    run_etl


