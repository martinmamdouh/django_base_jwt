import requests
r=requests.post('http://127.0.0.1:8000/api-auth/token/',data={"username": "martin", "password": ""})
print(r.text)