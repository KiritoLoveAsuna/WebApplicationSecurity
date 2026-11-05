# Asymmetric encryption
>In public key cryptography, the encryption key is different from the decryption key, which is why it is also called asymmetric encryption. Each participant owns a key pair consisting of a public key used for encryption and a private key or secret key used for decryption. As its name suggests, the public key is publicly known, allowing anyone to use it to encrypt messages intended for the owner of the corresponding private key. Since messages encrypted with a public key can be decrypted only with the corresponding private key, only the intended recipient can decrypt them

# Digital Signature
>When using digital signatures, messages are signed with the private key and verified with the public key, enabling anyone to verify that the signature was computed by the owner of the corresponding private key

# Certificates
>Consider an example where the user Alice wants to communicate with hackthebox.com privately. To do so, she obtains the public key of hackthebox.com, encrypts her message with it, and sends it to the target. Since only hackthebox.com knows the corresponding private key for decryption, the message cannot be decrypted by unauthorized actors. But how can Alice be sure that the public key actually belongs to hackthebox.com rather than to an attacker who wants to steal Alice's HackTheBox credentials? Assume an attacker intercepts Alice's request to obtain HackTheBox's public key and instead sends Alice his own public key while spoofing the origin to make Alice think it's actually HackTheBox's public key. She would then encrypt her message with the attacker's public key, enabling the attacker to decrypt and access the message. Certificates exist precisely to solve this problem

>The purpose of certificates is to bind a public key to an identity, thereby proving the identity of the public key owner and solving the previously discussed problem

# Certificate Authorities
>Certificate binds an identity, in this case HackTheBox, to the specific public key. But who can issue certificates? And what prevents an attacker from simply creating a certificate with their own public key for the domain hackthebox.com, thereby impersonating HackTheBox with a forged certificate? That is where Certificate Authorities come into play.

>Certificate authorities (CAs) are entities explicitly authorized to issue certificates. They do this by cryptographically signing a certificate. The identity of the CA is proven by a CA Certificate. Just like any other certificate, CA certificates are signed by another CA. This process continues until a root CA is reached. The chain from the root CA to the end-user's certificate is referred to as the certificate chain. When we look again at HackTheBox's certificate, we can see the certificate chain consisting of three total certificates at the top:

<img width="1416" height="175" alt="image" src="https://github.com/user-attachments/assets/3bbbe24a-465a-4fe0-b5a8-744f6cf65b0e" />

>When accessing a website, the browser validates the whole certificate chain. If any certificate in the chain is invalid or insecure, the browser displays a warning to the user. The root CA's identity is checked against the operating system's or web browser's trust store, a curated list of trusted root CAs maintained by vendors.

# openssl
PEM to DER
```
openssl x509 -outform der -in hackthebox.pem -out hackthebox.der
```
PEM to PKCS#7
```
openssl crl2pkcs7 -nocrl -certfile hackthebox.pem -out hackthebox.p7
```
