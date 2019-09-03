import requests
r = requests.post('http://127.0.0.1:8090/api-auth/token/',
                  data={"username": "martin", "password": "EWQ#ewq3"})
print(r.text)
