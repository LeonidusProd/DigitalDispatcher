FROM python:3.11.7-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /temp/requirements.txt

RUN pip install --upgrade pip; pip install -r /temp/requirements.txt

COPY ./backend_config ./backend_config/
COPY ./api_v1 ./api_v1/
COPY ./media ./media/
COPY ./static ./static/

COPY ./.env .env
COPY ./digdispdata.json digdispdata.json
COPY ./manage.py manage.py