FROM python:3

WORKDIR /habits_app

COPY ./requirements.txt /code/

RUN pip install -r /code/requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1
