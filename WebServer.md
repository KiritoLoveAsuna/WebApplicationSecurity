# Nginx
### Nginx Config location
```
/etc/nginx/nginx.conf
```
# Apache
### Apache Config location
```
/etc/apache2/apache2.conf
```
# IIS
### IIS Config Location
```
%WinDir%\System32\Inetsrv\Config\ApplicationHost.config
```
# Vhost
### Vhost Config Location
```
Vhosts Configuration:
/etc/apache2/sites-available/your_domain_1.conf
<VirtualHost *:80>
  ...
    ServerAdmin admin@your_domain_1
    ServerName your_domain_1
    ServerAlias www.your_domain_1
    DocumentRoot /var/www/your_domain_1/public_html
    ...
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
    ...
</VirtualHost>
```
