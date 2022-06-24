#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import uptrace
from opentelemetry.instrumentation.django import DjangoInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
    from django.conf import settings

    uptrace.configure_opentelemetry(
        dsn=settings.UPTRACE_DSN,
        service_name="backend",
        service_version="v0.1.0",
    )
    LoggingInstrumentor().instrument(set_logging_format=True)
    DjangoInstrumentor().instrument()
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
