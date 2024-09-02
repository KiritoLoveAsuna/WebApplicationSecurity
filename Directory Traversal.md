### Linux(../)
```
/etc/passwd

look for ssh private key files:
ssh-keygen --help
[-t dsa | ecdsa | ecdsa-sk | ed25519 | ed25519-sk | rsa]
id_dsa/ecdsa/ecdsa-sk/ed25519/ed25519-sk/rsa

if needed passphrase, ssh2john id_ecdsa > id_ecdsa.hash use john
```
### Windows(..\\)
```
C:\Windows\System32\drivers\etc\hosts

IIS Web Server:
C:\inetpub\logs\LogFiles\W3SVC1\
C:\inetpub\wwwroot\web.config
```

### Evade
```
url encoding
. -> %2e
/ -> %2f
```

### Dictionary
>Remember to add machine name to the directory list

/usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt  
/usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt  
/usr/share/dirb/wordlists/big.txt  
/usr/share/dirb/wordlists/common.txt
### Dirsearch
```
1. dirsearch -u url
2. dirsearch -u url -r (sometimes some path hidden behine 403 response )
3. dirsearch -u url -t 10 --timeout=30 -w wordlist(sometimes request will timeout if thread is default 25)
```
### gobuster
```
gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -q --no-error -u http://192.168.124.101:8080 --exclude-length 871 -t 200 -o result.txt
```
