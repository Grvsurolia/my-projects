import os

os.system('python manage.py makemigrations attendance employees leave news')
os.system('python manage.py migrate')
os.system('python manage.py runserver')