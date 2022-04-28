from django.core import management
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Produce client-side JS files"

    def handle(self, *args, **options):
        management.call_command("export_choices")
        management.call_command("graphql_schema")
