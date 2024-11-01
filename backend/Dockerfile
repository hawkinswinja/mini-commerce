FROM python:alpine3.20 AS base
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt --no-cache-dir


FROM python:alpine3.20
LABEL "author"="Gilbert Winja"
LABEL "description"="Dockerfile for Minicommerce backend"
USER 1234
COPY --from=base /usr/local/lib/python3.*/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=base /usr/local/bin /usr/local/bin
EXPOSE 8000
WORKDIR /app
COPY . .
CMD ["gunicorn", "-b", "0.0.0.0:8000", "-w", "4", "--log-level", "debug", "--access-logfile", "-", "minicommerce.wsgi"]