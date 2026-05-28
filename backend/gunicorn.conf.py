import multiprocessing
import os

# ── Tell the app it is managed by Gunicorn ───────────────────────────────────
# This must be set at module level (before workers are forked) so that
# AppConfig.ready() can skip its own tracing init and defer to post_fork.
os.environ["GUNICORN_MANAGED"] = "true"

# ── gunicorn ────────────────────────────────────────────────────────────
bind = os.environ.get("GUNICORN_BIND", "0.0.0.0:8000")
workers = int(os.environ.get("GUNICORN_WORKERS", multiprocessing.cpu_count() * 2 + 1))
worker_class = "sync"
timeout = int(os.environ.get("GUNICORN_TIMEOUT", 30))

# ── Logging ──────────────────────────────────────────────────────────────────
accesslog = "-"    # stdout
errorlog = "-"     # stdout
loglevel = os.environ.get("GUNICORN_LOG_LEVEL", "info")

# ── OpenTelemetry ─────────────────────────────────────────────────────────────
# Each Gunicorn worker is a *forked* child process.
# The TracerProvider must be initialised AFTER the fork — never before —
# because forking after SDK init causes broken background threads.
def post_fork(server, worker):
    """Called once per worker after fork(). Safe place to init the SDK."""
    from minicommerce.telemetry import configure_tracing
    configure_tracing()
    server.log.info("OTel tracing initialised in worker pid=%s", worker.pid)