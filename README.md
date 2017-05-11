# Dépenses.py

The purpose of this web app is to organize a budget within a group with shared expenditures.

## Features

 - Keep track of expenditures and reimbursements within groups
 - Calculates who owns money to who (takes expentidures and reimbursements in account)
 - Very easy to use account system

## Author
Yann Pellegrini <mail@yann-p.fr>

## Licence
GPLv3

## Database

see `tables.sql` to setup the database.

![schema](tables.png)

## Dependencies

 - flask
 - mysqlclient

```
sudo apt-get install python3-pip
sudo apt-get install python-dev python3-dev
sudo apt-get install libmysqlclient-dev
pip3 install flask
pip3 insall mysqlclient
```

## Running

```
cd src
./app.py   # or: python3.4 app.py

```

## Deploying on Apache

sudo apt-get install libapache2-mod-wsgi-py3

/etc/apache2/sites-available/depenses.conf:

```
<virtualhost *:80>
    ServerName vps.yann-p.fr # or localhost

    WSGIDaemonProcess webtool user=www-data group=www-data threads=5 home=/var/www/html/depenses
    WSGIScriptAlias /depenses /var/www/html/depenses/app.wsgi
    WSGIApplicationGroup %{GLOBAL}
    <directory /var/www/html/depenses>
         WSGIProcessGroup webtool
         WSGIApplicationGroup %{GLOBAL}
         WSGIScriptReloading On
         Order deny,allow
         Allow from all
     </directory>

     # Serve static files

     Alias "/depenses/static/" "/var/www/html/depenses/src/static/"
     <Directory "/var/www/html/depenses/src/static/">
          Order allow,deny
          Allow from all
     </Directory>
</virtualhost>
```