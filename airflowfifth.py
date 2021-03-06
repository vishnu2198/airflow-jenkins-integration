from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
#from airflow.operators import MultiplyBy5Operator

def print_hello():
 return 'Hello Wolrd'

dag = DAG('vishnu_DAG_6', description='Hello world example', schedule_interval='0 12 * * *', start_date=datetime(2017, 3, 20), catchup=False)
dummy_operator = DummyOperator(task_id='dummy_task', retries = 3, dag=dag)
hello_operator = PythonOperator(task_id='six_task', python_callable=print_hello, dag=dag)
dummy1_operator = DummyOperator(task_id='dummy_task_1', retries = 3, dag=dag)
dummy2_operator = DummyOperator(task_id='dummy_task_2', retries = 3, dag=dag)
dummy_operator >> hello_operator >> dummy1_operator >> dummy2_operator
