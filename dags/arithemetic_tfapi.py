'''
Task flow API allows us to use decorators instead of operators such as PythonOperator

Task 1: to start with a number(say 100)
task 2 : add 50 to that number
task 3 : to multiply the result by 2
task 4 : divide the result by 10

'''
from airflow import DAG
from airflow.decorators import task
from datetime import datetime

with DAG(
    dag_id="arithemetic_operator_tfapi"
)as dag:
    
    #Task 1: to start with a number(say 100)
    @task
    def start_number():
        initial_value=100
        print(f"starting_number: {initial_value}")
        return initial_value
    #task 2 : add 50 to that number
    @task
    def add_fifty(number):
        new_value=number+50
        print(f"add fifty:{number}+50={new_value}")
        return new_value
    #task 3 : to multiply the result by 2
    @task
    def multiply_two(number):
        new_value=number*2
        print(f"multiply two:{number}*2={new_value}")
        return new_value
    #task 4 : divide the result by 10
    @task
    def divide_ten(number):
        new_value=number/10
        print(f"divide ten:{number}/10={new_value}")
        return new_value
    #dependencies
    start_value =start_number()
    second_value=add_fifty(start_value)
    third_value=multiply_two(second_value)
    fourth_value=divide_ten(third_value)
