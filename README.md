## Deploying on Apache

```
<virtualhost *:80>
    ServerName localhost
 
    WSGIDaemonProcess webtool user=www-data group=www-data threads=5 home=/var/www/html/depenses/src
    WSGIScriptAlias /myapp /var/www/html/depenses/app.wsgi
 
    <directory /var/www/html/depenses/src>
        WSGIProcessGroup webtool
        WSGIApplicationGroup %{GLOBAL}
        WSGIScriptReloading On
        Order deny,allow
        Allow from all
    </directory>

    Alias "/myapp/static/" "/var/www/html/depenses/src/static/"
    <Directory "/var/www/html/depenses/src/static/">
        Order allow,deny
        Allow from all
    </Directory>



</virtualhost>
```