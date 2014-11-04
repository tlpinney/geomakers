#!/bin/bash

# assuming you've alreay done git clone http://github.com/geomakers/geomakers_project.git ~/geomakers_project
sudo apt-get update;
sudo apt-get install -y curl vim git postgresql libpq-dev postgresql-server-dev-all python python-dev python-pip;
sudo -u postgres createdb geomakers;
sudo pip install psycopg2;
git clone http://github.com/django/django.git ~/django-trunk;
sudo pip install -e ~/django-trunk/;
sudo pip install beautifulsoup4;
sudo python ~/geomakers_site/geomakers_site/manage.py makemigrations
sudo -u postgres python ~/geomakers_site/geomakers_site/manage.py migrate
sudo -u postgres python ~/geomakers_project/geomakers_site/manage.py runserver
sudo -u postgres python ~/geomakers_project/geomakers_site/manage.py createsuperuser;
