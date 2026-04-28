https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SQL%20Injection
# Categories
### Error-Based

### Union-Based


### Blind Sql Injection
###### Time-Based
###### Boolean-Based
###### Out of Band 

### Auth Bypass with or 
<img width="3217" height="497" alt="image" src="https://github.com/user-attachments/assets/33d19073-5bcf-45ad-939e-3692666328e3" />
>We were able to log in successfully as admin. However, what if we did not know a valid username? Let us try the same request with a different username this time.
<img width="3302" height="482" alt="image" src="https://github.com/user-attachments/assets/c10692d3-7a44-4d23-bad7-cdbc3bd2e168" />
>The login failed because notAdmin does not exist in the table and resulted in a false query overall.
<img width="1740" height="881" alt="image" src="https://github.com/user-attachments/assets/f3e2158a-5da6-4862-9a55-401958e2d96e" />
>To successfully log in once again, we will need an overall true query. This can be achieved by injecting an OR condition into the password field, so it will always return true. Let us try something' or '1'='1 as the password.
<img width="3578" height="523" alt="image" src="https://github.com/user-attachments/assets/899d7d65-3078-4598-aaed-324c79056b65" />
