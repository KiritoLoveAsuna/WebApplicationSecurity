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
### Asymmetric JWT Token Verify
```
import jwt
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicNumbers
import base64
import json

# RS256 JWT
jwt_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHVkZW50IiwibmFtZSI6IlN0dWRlbnQiLCJvZmZzZWM6a2V5IjoidmFsdWUifQ.ubg1sGpDDtWeTWvE_-edPqwa9lV6x1XVHRM_MYparWyNqu6fdxpUhwhf1WUrIYQb7UebHo8kpQ4ZW5hBY2aHImESEvMuYV_mzCD9PYmSUH0OlRPm8c_B3GT2ojT3j13vq7DHKjPEvvHtHQ48J2g9Jr8gVJ-kePuqDyzMD7R-IDViMR5xM-U5_Q1BeYSZ31sU3j9MJWrqvPo8u2G_m6ZYKXIlhiDxKrCOlENSKhz0VG1wzIGnR7l2Wmx7jcqRZRIuA8RY2eClW1qCFippmJnjhSt1Kxnuo02mRt5G6lGtDoMyZsGz8kIR4dms5m8lYYkvatjEZWSnk0EHdrHuPRxYDg"
 
# JWK in string format
jwk_string = """{
    "kty": "RSA",
    "use": "sig",
    "alg": "RS256",
    "n": "xyl5YfLcmYxq7YfCrTnr29r7oaYCKcpxQtGA8DmD5dcG3sw9EVPEBVdTjUsTRyux2n48vCevNUDiwHnI3t3nTOfOppNJj4vxVBuuirMuIWU_NRxUAtkm6FAz4923F9faKJM_6iM-88rs_Wbo7_tGlE43wr0lQ5HTgTA6zu5IDGBomhRr6dCFPrDOPv7yzMsgKFbycZhxo1OAXbS6bGBMd0GzMQVrJ-XXXFDhYbwnSLdDn1aSopTMZerg4iZrUG0-tZCu-syA8NzHdbhZUCWVFbayQ3E5es3NRn5YBTzssGHxEHl58c3RtCR98mClcBQijL4eWSWVx3p3BxWjtiOKzQ",
    "e": "AQAB"
}"""
# Convert the JWK from string to dictionary
jwk = json.loads(jwk_string)

# Function to convert base64url encoding to base64 encoding
def base64url_to_base64(value):
    return base64.urlsafe_b64decode(value + '===')

# Extract the public key components
n = int.from_bytes(base64url_to_base64(jwk['n']), byteorder='big')
e = int.from_bytes(base64url_to_base64(jwk['e']), byteorder='big')

# Create the RSA public key
public_numbers = RSAPublicNumbers(e, n)
public_key = public_numbers.public_key(backend=default_backend())

# Convert the RSA public key to PEM format
pem_public_key = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Verify the JWT
try:
    decoded = jwt.decode(jwt_token, pem_public_key, algorithms=["RS256"])
    print("JWT verified successfully:", decoded)
except jwt.PyJWTError as e:
    print("Verification failed:", str(e))
```
### Symmetric JWT token without signature
```
1.change alg to none
2.change role and sub to other user
3. header.payload. = token
```
