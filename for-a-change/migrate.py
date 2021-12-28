import os

os.system("python manage.py makemigrations fundraiser donor adminapp")
os.system("python manage.py migrate")