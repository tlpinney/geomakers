###GeoMakers(Avalanche) Installation Guide

####Update
```
sudo apt-get update
```

####Install Required Packages
```
sudo apt-get install -y apache2-dev curl vim git postgresql libpq-dev postgresql-server-dev-all python python-dev python-pip
```
* apache2-dev: python_mod needs this
* curl: used to download from the internet
* gcc: python_mod uses this
* vim: used to edit files in terminal
* git: used to download code from github repositories
* postgresql: the database that stores the information
* libpq-dev: needed to install psycopg2 database adapater
* postgresql-server-dev-all: includes all postgres stuff needed; includes postgresql-server-dev-X.Y, which is needed to install psycopg2 database adapater
* python: code language that django uses
* python-dev: code language that django uses
* python-pip: used to install python packages

#### Create GeoMakers User for Ubuntu Machine
```
sudo adduser geomakers
```

#### Create geomakers User for Postgres
```
sudo -u postgres psql -c "CREATE USER geomakers;"
```

####Create Database
Create geomakers database
```
sudo -u postgres psql -c "CREATE DATABASE geomakers;"
```

####Change Ownership of geomakers database to the geomakers user
Create geomakers database
```
sudo -u postgres psql -c "ALTER DATABASE geomakers OWNER TO geomakers;"
```

###Install Psycopg
Psycopg is a PostgreSQL database adapater for Python
```
sudo pip install psycopg2;
```

####Download Django
Download the django code into the geomakers user's home directory. 
```
sudo -u geomakers git clone http://github.com/django/django.git /home/geomakers/django-trunk
```

####Make Django Code Importable
Make Django code importable into Python with the following
```
sudo pip install -e /home/geomakers/django-trunk/
```

###Install BeautifulSoup4
BeautifulSoup4 is used to get titles for links
```
sudo pip install beautifulsoup4;
```

####Download This Repo
```
sudo -u geomakers git clone http://github.com/geomakers/geomakers.git /home/geomakers/geomakers
```

####Create Database (db) Tables
The following command creates the tables needed by the INSTALLED_APPS.
```
sudo -u geomakers python /home/geomakers/geomakers/windwaker/manage.py makemigrations
sudo -u geomakers python /home/geomakers/geomakers/windwaker/manage.py migrate
```

####Create Admin User
The following command will prompt you for a username and email address.
Enter ```admin``` as username and enter your email address.
And enter your password twice.
```
sudo -u geomakers python /home/geomakers/geomakers/windwaker/manage.py createsuperuser;
```

####Install mod_python
This connects the django application to the apache server
```
sudo git clone https://github.com/grisha/mod_python /var/mod_python;
cd /var/mod_python;
sudo ./configure;
sudo make;
sudo make install;
```

####Modify Apache2 Config File, httpd.conf or apache2.conf
Add ```LoadModule python_module /usr/lib/apache2/modules/mod_python.so``` to apache2.conf


####Run the Development Server
```
sudo -u geomakers python /home/geomakers/geomakers/windwaker/manage.py runserver
```
