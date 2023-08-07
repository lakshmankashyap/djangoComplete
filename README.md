$ python3 -m venv env
$ source env/bin/activate
$ pip3 install Django
python3
Python 3.10.12 (main, Jun 11 2023, 05:26:28) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> django.__version__
'4.2.4'
>>> 
$ django-admin startproject core
$ cd env
$ python3 manage.py  startapp home
$ python3 manage.py  startapp accounts
python3 manage.py makemigrations
python3 manage.py migrate