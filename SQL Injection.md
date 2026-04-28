https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SQL%20Injection

# Login Sql Query
```
select * from logins where username = 'admin' and password = 'admin';
select * from logins where (username = 'admin' and id > 1) and password = 'admin';
```
# Note
>Note: In SQL, using two dashes only is not enough to start a comment. So, there has to be an empty space after them, so the comment starts with (-- ), with a space at the end. This is sometimes URL encoded as (--+), as spaces in URLs are encoded as (+). To make it clear, we will add another (-) at the end (-- -), to show the use of a space character.

>Tip: if you are inputting your payload in the URL within a browser, a (#) symbol is usually considered as a tag, and will not be passed as part of the URL. In order to use (#) as a comment within a browser, we can use '%23', which is an URL encoded (#) symbol.
# Categories
### Error-Based

### Union-Based


### Blind Sql Injection
###### Time-Based
###### Boolean-Based
###### Out of Band 

### Auth Bypass with or Operator
Thesis
>The MySQL documentation for operation precedence states that the AND operator would be evaluated before the OR operator. This means that if there is at least one TRUE condition in the entire query along with an OR operator, the entire query will evaluate to TRUE since the OR operator returns TRUE if one of its operands is TRU
<img width="3217" height="497" alt="image" src="https://github.com/user-attachments/assets/33d19073-5bcf-45ad-939e-3692666328e3" />
<img width="1700" height="881" alt="image" src="https://github.com/user-attachments/assets/a2ec4e73-c82f-4438-a495-252b30464eb8" />
>We were able to log in successfully as admin. However, what if we did not know a valid username? Let us try the same request with a different username this time.
<img width="3302" height="482" alt="image" src="https://github.com/user-attachments/assets/c10692d3-7a44-4d23-bad7-cdbc3bd2e168" />
>The login failed because notAdmin does not exist in the table and resulted in a false query overall.
<img width="1740" height="881" alt="image" src="https://github.com/user-attachments/assets/f3e2158a-5da6-4862-9a55-401958e2d96e" />
>To successfully log in once again, we will need an overall true query. This can be achieved by injecting an OR condition into the password field, so it will always return true. Let us try something' or '1'='1 as the password.
<img width="3578" height="523" alt="image" src="https://github.com/user-attachments/assets/899d7d65-3078-4598-aaed-324c79056b65" />
