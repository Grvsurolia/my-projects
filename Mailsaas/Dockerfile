FROM python:3.7-slim-buster
FROM node:14.4.0-buster-slim
EXPOSE 8000
COPY . /
WORKDIR /
RUN apt-get update
RUN apt-get install libpq-dev gcc python3-pip -y
RUN pip3 install -r requirements.txt
RUN npm i
RUN npm run build
CMD python3 manage.py runserver 0.0.0.0:8000