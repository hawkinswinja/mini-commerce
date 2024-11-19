FROM python:3.12-slim AS base
RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt --no-cache-dir


FROM python:3.12-slim
RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
USER nobody
COPY --from=base /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=base /usr/local/bin /usr/local/bin
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
EXPOSE 8000
COPY . /app/
CMD ["gunicorn", "-b", "0.0.0.0:8000", "-w", "4", "--log-level", "debug", "--access-logfile", "-", "minicommerce.wsgi"]