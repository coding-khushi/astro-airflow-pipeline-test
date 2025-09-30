'''
Task 1: to start with a number(say 100)
task 2 : add 50 to that number
task 3 : to multiply the result by 2
task 4 : divide the result by 10
'''
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

#define the function for each task
def start_number(**context):
    context["ti"].xcom_push(key="current_value",value=100)
    print("starting number is 100")

def add_fifty(**context):
    current_value=context["ti"].xcom_pull(key="current_value",task_ids="start_number")
    new_value=current_value+50
    context["ti"].xcom_push(key="current_value",value=new_value)
    print(f"add 50:{current_value}+50={new_value}")

def multipy_two(**context):
    current_value=context["ti"].xcom_pull(key="current_value",task_ids="add_fifty")
    new_value=current_value*2
    context["ti"].xcom_push(key="current_value",value=new_value)
    print(f"multipy by 2:{current_value}*2={new_value}")

def divide_ten(**context):
    current_value=context["ti"].xcom_pull(key="current_value",task_ids="multiply_two")
    new_value=current_value/10
    context["ti"].xcom_push(key="current_value",value=new_value)
    print(f"divide by 10:{current_value}/10={new_value}")

#define the DAG

with DAG(
    dag_id="arithematic_operations"
)as dag:
    start_number=PythonOperator(
        task_id="start_number" ,
        python_callable=start_number
        #provide_context=True
    )
    add_fifty=PythonOperator(
        task_id="add_fifty" ,
        python_callable=add_fifty
        #provide_context=True
    )
    multipy_two=PythonOperator(
        task_id="multiply_two" ,
        python_callable=multipy_two
        #provide_context=True
    )
    divide_ten=PythonOperator(
        task_id="divide_ten" ,
        python_callable=divide_ten
        #provide_context=True
    )
    #dependencies
    start_number >> add_fifty >>multipy_two >> divide_ten