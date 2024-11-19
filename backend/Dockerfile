FROM python:3.12-slim AS base
RUN apt-get update && apt-get install -y libpq-dev gcc
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir


FROM python:3.12-slim
RUN apt-get update && apt-get install -y libpq-dev
USER nobody
COPY --from=base /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=base /usr/local/bin /usr/local/bin
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
EXPOSE 8000
COPY . .
CMD ["gunicorn", "-b", "0.0.0.0:8000", "-w", "4", "--log-level", "debug", "--access-logfile", "-", "minicommerce.wsgi"]