FROM python:3.9-alpine

# FROM python:3.6-slim

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev redis 

RUN pip install --upgrade pip

COPY requirements.txt /code/

RUN pip install -r requirements.txt
COPY . /code/

EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]