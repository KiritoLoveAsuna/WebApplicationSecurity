### wfuzz
```
curl -s /dev/null http://idor-sandbox:80/user/?uid=91191 -w '%{size_download}' --header "Cookie: PHPSESSID=2a19139a5af3b1e99dd277cfee87bd64"
...
2873

wfuzz -c -z file,/usr/share/seclists/Fuzzing/5-digits-00000-99999.txt --hc 404 --hh 2873 -H "Cookie: PHPSESSID=2a19139a5af3b1e99dd277cfee87bd64" http://idor-sandbox:80/user/?uid=FUZZ
```
### Enumerating Vhosts
```
ffuf -u "http://flight.htb" -H "Host: FUZZ.flight.htb" -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -c -t 50 -fs 7069

Then add subdomain entry to /etc/hosts

Vhosts Configuration:
/etc/apache2/sites-available/your_domain_1.conf
<VirtualHost *:80>
  ...
    ServerAdmin admin@your_domain_1
    ServerName your_domain_1
    ServerAlias www.your_domain_1
    DocumentRoot /var/www/html
    ...
</VirtualHost>
```
