#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'minicommerce.settings')
    try:
        from opentelemetry import trace, metrics, _logs
        from opentelemetry.sdk.resources import Resource
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import BatchSpanProcessor
        from opentelemetry.sdk.metrics import MeterProvider
        from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
        from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
        from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
        from opentelemetry.instrumentation.django import DjangoInstrumentor

        # 0. Define common Resource properties (Service Name)
        service_name = os.environ.get("OTEL_SERVICE_NAME", "django_app")
        resource = Resource.create({"service.name": service_name})
        
        # Pull your config settings from .env
        traces_exporter_env = os.environ.get("OTEL_TRACES_EXPORTER", "otlp").lower()
        metrics_exporter_env = os.environ.get("OTEL_METRICS_EXPORTER", "otlp").lower()
        logs_exporter_env = os.environ.get("OTEL_LOGS_EXPORTER", "otlp").lower()
        is_grpc = os.environ.get("OTEL_EXPORTER_OTLP_PROTOCOL") == "grpc"

        # =====================================================================
        # 1. TRACES PIPELINE
        # =====================================================================
        if traces_exporter_env != "none":
            trace_provider = TracerProvider(resource=resource)
            trace.set_tracer_provider(trace_provider)
            
            if traces_exporter_env == "console":
                from opentelemetry.sdk.trace.export import ConsoleSpanExporter
                trace_exporter = ConsoleSpanExporter()
            else:
                if is_grpc:
                    from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
                else:
                    from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
                trace_exporter = OTLPSpanExporter()
                
            trace_provider.add_span_processor(BatchSpanProcessor(trace_exporter))

        # =====================================================================
        # 2. METRICS PIPELINE
        # =====================================================================
        if metrics_exporter_env != "none":
            if metrics_exporter_env == "console":
                from opentelemetry.sdk.metrics.export import ConsoleMetricExporter
                metric_exporter = ConsoleMetricExporter()
            else:
                if is_grpc:
                    from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
                else:
                    from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
                metric_exporter = OTLPMetricExporter()
                
            reader = PeriodicExportingMetricReader(metric_exporter)
            metric_provider = MeterProvider(resource=resource, metric_readers=[reader])
            metrics.set_meter_provider(metric_provider)

        # =====================================================================
        # 3. LOGS PIPELINE
        # =====================================================================
        if logs_exporter_env != "none":
            log_provider = LoggerProvider(resource=resource)
            _logs.set_logger_provider(log_provider)
            
            if logs_exporter_env == "console":
                from opentelemetry.sdk._logs.export import ConsoleLogRecordExporter
                log_exporter = ConsoleLogRecordExporter()
            else:
                if is_grpc:
                    from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter
                else:
                    from opentelemetry.exporter.otlp.proto.http._log_exporter import OTLPLogExporter
                log_exporter = OTLPLogExporter()
                
            log_provider.add_log_record_processor(BatchLogRecordProcessor(log_exporter))
            
            # Inject OTel handler into standard Python logging
            import logging
            handler = LoggingHandler(level=logging.NOTSET, logger_provider=log_provider)
            logging.getLogger().addHandler(handler)

        # =====================================================================
        # 4. INSTRUMENT DJANGO
        # =====================================================================
        DjangoInstrumentor().instrument()
        print("→ OTel Manual Pipeline: Fully and safely initialized.")
    except ImportError as e:
        print(f"OTel not initialized: {e}")
        
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
