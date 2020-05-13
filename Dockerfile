FROM python:3.7-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /srv/app/

COPY requirements.txt /srv/app/

RUN apt-get -y -qq update \
    && apt-get -y -qq upgrade \
    && pip install --no-cache-dir -r requirements.txt

COPY . /srv/app/
