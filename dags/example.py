from airflow.decorators import dag, task
from include.operators import PublishEventOperator, WaitForEventOperator
from pendulum import datetime


@dag(start_date=datetime(2024, 1, 1), schedule="@daily", catchup=False)
def example_publish():
    @task
    def first_task():
        print("First task")

    my_publish_task = PublishEventOperator(
        task_id="publish_event", event_name="my_event"
    )

    first_task() >> my_publish_task


example_publish()


@dag(start_date=datetime(2024, 1, 1), schedule="@daily", catchup=False)
def example_wait():
    my_wait_task = WaitForEventOperator(task_id="wait_event", event_name="my_event")

    @task
    def some_task():
        print("Some task")

    my_wait_task >> some_task()


example_wait()
