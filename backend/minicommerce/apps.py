import os
from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = "minicommerce"
    default_auto_field = "django.db.models.BigAutoField"

    def ready(self) -> None:
        from opentelemetry.instrumentation.django import DjangoInstrumentor
        DjangoInstrumentor().instrument()

        # Gunicorn initialises tracing per-worker in post_fork (fork-safe).
        # Every other runner (manage.py runserver, pytest, celery, etc.)
        # gets it here instead.
        if not os.environ.get("GUNICORN_MANAGED"):
            from minicommerce.telemetry import configure_tracing
            configure_tracing()