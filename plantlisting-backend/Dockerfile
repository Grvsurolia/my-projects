FROM python:3.6

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# ENV DEBUG 0

# install psycopg2
# RUN apt update \
#     && apt add --virtual build-deps gcc python3-dev musl-dev \
#     && apt add postgresql-dev \
#     && pip install psycopg2 \
#     && apt del build-deps


ADD . /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt
# RUN python manage.py collectstatic
RUN python manage.py makemigrations && python manage.py migrate

COPY . /app/ 

CMD gunicorn Plant_Listing.wsgi:application --bind 0.0.0.0:$PORT

# CMD gunicorn --bind 0.0.0.0:$PORT config.wsgi