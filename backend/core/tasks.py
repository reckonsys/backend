from celery import shared_task


@shared_task
def print_data(data):
    print(f"Data: {data}")
