import logging
import os

from opentelemetry import trace
from opentelemetry.sdk.resources import Resource, SERVICE_NAME, SERVICE_VERSION
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
    SimpleSpanProcessor,
)

logger = logging.getLogger(__name__)


def _build_resource() -> Resource:
    """Builds the resource descriptor attached to every span."""
    return Resource.create(
        {
            SERVICE_NAME: os.environ.get("OTEL_SERVICE_NAME", "minicommerce_api"),
            SERVICE_VERSION: os.environ.get("APP_VERSION", "1.0.0"),
            "deployment.environment": os.environ.get("APP_ENV", "development"),
        }
    )


def configure_tracing() -> None:
    """
    Initialise the global TracerProvider.

    Behaviour is driven entirely by environment variables so no code
    changes are needed to switch between dev and prod:

        APP_ENV=development  → ConsoleSpanExporter  (stdout, human-readable)
        APP_ENV=production   → OTLPSpanExporter      (gRPC to collector)

    Call this ONCE per process (Gunicorn worker post_fork hook handles that).
    """
    app_env = os.environ.get("APP_ENV", "development")

    provider = TracerProvider(resource=_build_resource())

    if app_env == "production":
        _attach_otlp_exporter(provider)
    else:
        _attach_console_exporter(provider)

    trace.set_tracer_provider(provider)

    logger.info("OpenTelemetry tracing configured [env=%s]", app_env)


def _attach_otlp_exporter(provider: TracerProvider) -> None:
    """Sends spans over gRPC to an OTel Collector / Jaeger / Tempo."""
    from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

    endpoint = os.environ.get("OTEL_EXPORTER_OTLP_ENDPOINT", "http://otel-collector:4317")

    exporter = OTLPSpanExporter(
        endpoint=endpoint,
        # insecure=True is fine inside a private Docker network;
        # set OTEL_EXPORTER_OTLP_INSECURE=false and provide certs for public endpoints.
        insecure=os.environ.get("OTEL_EXPORTER_OTLP_INSECURE", "true").lower() == "true",
    )

    # BatchSpanProcessor buffers & sends in background threads — correct for prod.
    provider.add_span_processor(BatchSpanProcessor(exporter))
    logger.info("OTLP exporter attached [endpoint=%s]", endpoint)


def _attach_console_exporter(provider: TracerProvider) -> None:
    """Prints spans to stdout — great for local dev / CI."""
    # SimpleSpanProcessor flushes synchronously on every span — fine for dev.
    provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))
    logger.info("Console span exporter attached")