# MailSaaS

## Installation
```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
npm install
npm run dev-watch
python manage.py runserver

## Running Celery

Celery can be used to run background tasks. To run it you can use:

Add these to WeekDays Table :
"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"

```bash
celery -A mail beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
celery -A mail worker -l INFO
```
## Getting Started with Docker

These instructions will cover usage information and for the docker container 


### Prerequisities

In order to run this container you'll need docker installed.

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

#### Commands for this project

- For create and start container and build images

```bash
docker-compose up --build    
```
###  Create superuser on Docker

```bash
docker-compose run web python3 manage.py createsuperuser
```

- For start specific service 

```bash
docker-compose up <service name>
```

- For view images
```bash
docker-compose images
```

- For view containers

```bash
docker-compose ps
```

- For stop services
```bash
docker-compose stop
```

- For kill services
```bash
docker-compose kill
```

- For remove stopped containers
```bash
docker-compose rm
```

- For stop all containers and remove images, volumes
```bash
docker-compose down
```