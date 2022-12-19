# Lab 28: Authentication & Production Server

# Author: Mohammad Alfayoume

## Username and Password

1. superuser: username: admin , password: admin

## runserver

`docker-compose up --build`

## create superuser
`docker-compose run web python manage.py createsuperuser`

## makemigrations
`docker-compose run web python manage.py makemigrations`

## migrate
`docker-compose run web python manage.py migrate`

## Test
`docker-compose run web python manage.py test`
