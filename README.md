# PERSONAL PORTFOLIO WITH DJANGO 
This is a portfolio pproject with Django5.0, a python framwork for Web application development.

# Run Locally

## Requirements
 - Linux OS (if you don't have it, install it; if you can't use it, raise your skills)
 - Python (pre-installed on most Linux distributions)
 - Postgresql 12 or higher (you can use another SGBD but you will need to configure the settings.py file accordingly)

## Instructions

Clone the project  
~~~bash  
  git clone https://github.com/Serj-crypto/PORTFOLIO-DJANGO-APP.git
~~~

Go to the project directory  
~~~bash  
  cd PORTFOLIO-DJANGO-APP
~~~

Create a virtual environment:   
_if not installed, install virtualenv using this command:_
~~~bash
  python3 -m pip install virtualenv
~~~
then create your virtual environment _(here named .env)_
~~~terminal
  virtualenv .env
~~~

Activate your virtual environment
~~~bash 
source .env/bin/activate
~~~

Install the Requirements

~~~bash  
  pip install -r requirements.txt
~~~

Create a Postgres DB  
Configure a user and a password for the project

go to the directory portfolio of the project.
~~~bash
  cd portfolio/portfolio
~~~

create a .env file and configure those parameters:
~~~bash
DEBUG = "True"
NAME  = "<bd_name>"
USER = "<user_name>"
PASSWORD = "***********"
HOST = "localhost"
PORT = "5432"
SECRET_KEY = "************************************************************"
~~~

_(to generate a secret key, you can open a python terminal and type those comand lines below):_
~~~bash
$ python
>>> from django.core.management import utils
>>> print(utils.get_random_secret_key())
~~~

Apply migrations and migrate
~~~bash
python manage.py makemigrations
python manage.py migrate
~~~

Create a superuser
~~~bash
  python manage.py createsuperuser
~~~



# Contributing  

Contributions are always welcome!  

See my [github profile](https://github.com/Serj-crypto)

# License  

[MIT](https://choosealicense.com/licenses/mit/)

# Authors

- Serginau LOUIS