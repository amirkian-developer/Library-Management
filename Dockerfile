FROM python:3.12.4-slim-bookworm

ENV PYTHONUNBUFFERED 1

WORKDIR /src/usr/app

COPY requirements.txt .

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt 

COPY . .

