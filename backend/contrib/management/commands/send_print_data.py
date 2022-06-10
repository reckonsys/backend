from django.core.management.base import BaseCommand

from backend.celery import app


class Command(BaseCommand):
    help = "Send Print data task"

    def handle(self, *args, **options):
        app.send_task("backend.core.tasks.print_data", kwargs={"data": "foo"})
