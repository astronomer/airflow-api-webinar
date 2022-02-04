from airflow.decorators import dag, task

from datetime import datetime
import time
from random import randrange


@dag(schedule_interval='0 */4 * * *', start_date=datetime(2022, 2, 3), catchup=True)
def random_failures():

    @task(task_id='random-task', retries=0)
    def random_number():
        time.sleep(10)
        number = randrange(100)
        print(number)
        if number > 50:
            raise Exception

    random_number()
        
dag = random_failures()