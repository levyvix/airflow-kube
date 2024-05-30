from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago

default_args = {
	'owner': 'airflow',
	'depends_on_past': False,
	'start_date': days_ago(2),
	'email': [''],
	'email_on_failure': False,
	'email_on_retry': False,
	'retries': 1,
	'retry_delay': 300,
	'catchup': False
}

with DAG('01_dummy_dag', default_args=default_args, schedule_interval=None) as dag:
	dummy = DummyOperator(task_id='dummy', dag=dag)
 
