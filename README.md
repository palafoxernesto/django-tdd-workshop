# simple-blog-with-django

This is a simple blog built with Django 

## Seting up environment

I recommend using virtualenv. Once you have your env active go to the root of the project in the command line and type:

```
pip install -r requirements.txt
```
This will install all the dependencies needed inside your virtualenv.

## Creating DB and super user
You need to run the migrations first, so go to /myblog folder and then type:
```
python3 manage.py migrate
```
and 
```
python manage.py createsuperuser
```
to create super user

## Run dev server
Everything is ok to run the project now. In the same folder /myblog just type:

```
python3 manage.py runserver
```
The development server should be running now at: [http://127.0.0.1:8000](http://127.0.0.1:8000)