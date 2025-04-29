from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from scripts.main import get_data, format_data, stream_data


default_args={
        'owner': 'airflow',
        'start_date': datetime(2023, 10, 1),
        'retries': 0,
    }

with DAG(   
    dag_id="run_main_script_daily",
    default_args=default_args,
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
) as dag:

    process_kafka_task = PythonOperator(
        task_id="run_main_py",
        python_callable=stream_data, 
        dag=dag
    )

print("DAG created successfully")