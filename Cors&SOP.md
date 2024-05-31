### Same Origin Policy 
```
URL	RESULT	REASON
https://foo.com/myInfo	Allowed	Same Origin
http://foo.com/users.json	Blocked	Different Scheme and Port
https://api.foo.com/info	Blocked	Different Domain
https://foo.com**:8443**/files	Blocked	Different Port
https://bar.com/analytics.js	Blocked	Different Domain
```
### curl requesting cors settings
```
curl -v -X OPTIONS http://192.168.154.155/exercise2
```
