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
sudo useradd geomakers
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

###Install Python requirements
```
sudo pip install -r requirements.txt
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
sudo -u geomakers python /home/geomakers/geomakers/windwaker/manage.py createsuperuser
```

####Install WSGI
```
sudo apt-get install libapache2-mod-wsgi
```

####Copy Over Apache 2 Config File to Site-Enabled Directory
```
sudo cp /home/geomakers/geomakers/geomakers.conf /etc/apache2/sites-available/geomakers.conf
```

####Create symbolic link
```
sudo ln -s /etc/apache2/sites-available/geomakers.conf /etc/apache2/sites-enabled/geomakers.conf
```

####Restart Apache
```
sudo service apache2 restart
```



####Run the Development Server
```
sudo -u geomakers python /home/geomakers/geomakers/geomakers/windwaker/manage.py runserver
```
