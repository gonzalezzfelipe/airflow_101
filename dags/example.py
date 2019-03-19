import datetime as dt

from airflow import DAG

from operators.today_operator import TodayOperator
from sensors.prime_minute_sensor import PrimeMinuteSensor

dag = DAG(
    dag_id='test_custom_sensor_and_operator',
    start_date=dt.datetime(2019, 3, 19, 13),
    schedule_interval='2 * * * *',
    catchup=True)

with dag:
    sense = PrimeMinuteSensor(
        task_id='check_minute_for_prime_number',
        poke_interval=60,
        timeout=60 * 60)
    execute = TodayOperator(task_id='print_now_and_execution_date')

    sense >> execute
