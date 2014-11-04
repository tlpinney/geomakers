###GeoMakers(Avalanche) Installation Guide

####Update
```
sudo apt-get update
```

####Install Required Packages
```
sudo apt-get install -y curl vim git postgresql libpq-dev postgresql-server-dev-all python python-dev python-pip
```
* curl: used to download from the internet
* vim: used to edit files in terminal
* git: used to download code from github repositories
* postgresql: the database that stores the information
* libpq-dev: needed to install psycopg2 database adapater
* postgresql-server-dev-all: includes all postgres stuff needed; includes postgresql-server-dev-X.Y, which is needed to install psycopg2 database adapater
* python: code language that django uses
* python-dev: code language that django uses
* python-pip: used to install python packages

####Create Database
You will now create the databse that the geomakers_app will use.  The database is called geomakers.
```
sudo -u postgres createdb geomakers;
```

###Install Psycopg
Psycopg is a PostgreSQL database adapater for Python
```
sudo pip install psycopg2;
```

####Download Django
The following code will download the django code into the current user's home directory. 
```
git clone http://github.com/django/django.git ~/django-trunk
```

####Make Django Code Importable
Make Django code importable into Python with the following
```
sudo pip install -e ~/django-trunk/
```

###Install BeautifulSoup4
BeautifulSoup4 is used to get titles for links
```
sudo pip install beautifulsoup4;
```

####Download This Repo
```
git clone http://github.com/geomakers/geomakers_project.git ~/geomakers_project
```

####Create Database (db) Tables
The following command creates the tables needed by the INSTALLED_APPS.
```
sudo python ~/geomakers_site/geomakers_site/manage.py makemigrations
sudo -u postgres python ~/geomakers_site/geomakers_site/manage.py migrate
```

####Run the Development Server
```
sudo -u postgres python ~/geomakers_project/geomakers_site/manage.py runserver
```

####Create Admin User
The following command will prompt you for a username and email address.
Enter ```admin``` as username and enter your email address.
And enter your password twice.
```
sudo -u postgres python ~/geomakers_project/geomakers_site/manage.py createsuperuser;
```
