#    __Employee-Management-System__ 

>The employee management system maintains the professional and personal details of the employees and the company in a safe manner.
> EMS helps to eliminate the manual process and saves a lot of time and money.this system is a distributed system developed to     maintain the employee details and the company workflow process systematically.

## ___Functionality___

- Employees Registration and login
- Employees attendance system
- Employees leaves 
- Employee calender system
- Notification for every employee of every updates
- Company forms and policy
- Comapny news and updates


## ___Project run and setup___ 

- Ensure you have python3 installed
- Clone the project repository 
- Create a virtual environment using `python3 -m virtualenv venv`
- Activate the virtual environment by running source `venv/bin/activate`
- Install the dependencies using `pip install -r requirements.txt`
- Migrate existing db tables by running `python manage.py migrate`
- Run the django development server using `python manage.py runserver`


## Commands for run Celery

> celery -A employee_managements worker -l info

> celery -A employee_managements beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler


