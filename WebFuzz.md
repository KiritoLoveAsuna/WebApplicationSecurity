### wfuzz
```
curl -s /dev/null http://idor-sandbox:80/user/?uid=91191 -w '%{size_download}' --header "Cookie: PHPSESSID=2a19139a5af3b1e99dd277cfee87bd64"
...
2873

wfuzz -c -z file,/usr/share/seclists/Fuzzing/5-digits-00000-99999.txt --hc 404 --hh 2873 -H "Cookie: PHPSESSID=2a19139a5af3b1e99dd277cfee87bd64" http://idor-sandbox:80/user/?uid=FUZZ
```
### Enumerating Vhosts
```
ffuf -u "http://flight.htb" -H "Host: FUZZ.flight.htb" -w dic -c -t 50 -fs 7069(filter response size)
ffuf -u "http://flight.htb" -H "Host: FUZZ.flight.htb" -w dic -c -t 50 -fw 20(filter words)
ffuf -u "http://flight.htb" -H "Host: FUZZ.flight.htb" -w dic -c -t 50 -fc 20(filter status codes)

Then add subdomain entry to /etc/hosts

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
