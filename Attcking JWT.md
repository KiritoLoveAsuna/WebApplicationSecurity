### JWT 
JWTs are typically comprised of three sections: header, payload, and signature. The sections of a JWT are independently-encoded using Base64URL and concatenated using a period (.) as a separator  
>We need to note that Base64URL is slightly different than Base64, as it tries to avoid characters such as =, /, and +, which would be problematic if they were part of a URL.

![image](https://github.com/KiritoLoveAsuna/WebApplicationSecurity/assets/38044499/9ca79357-5ed1-4b29-b6c4-068fd252008a)

### Calculation of Signature with symmetric key
```
import hashlib
import hmac
import base64
jwt_header="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
jwt_payload="eyJzdWIiOiJzdHVkZW50IiwibmFtZSI6IlN0dWRlbnQiLCJpYXQiOjE1MTYyMzkwMjJ9"
key="studentlab"
message = jwt_header + "." + jwt_payload
signature = hmac.new(key.encode(), message.encode(), hashlib.sha256).digest()
signature_encoded = base64.urlsafe_b64encode(signature).decode().rstrip("=")
print(signature_encoded)
```
### symmetric cryptography algorithms
```
Hash-based Message Authentication Code (HMAC) using SHA-256 hashing algorithm (HS256)
HMACs with SHA-384 (HS384) or SHA-512 (HS512)
```
### Asymmetric cryptography algorithms
```
RSA (RS256)
Elliptic Curves (ES256)
```

