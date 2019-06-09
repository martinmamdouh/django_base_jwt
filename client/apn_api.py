import requests
headers={'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwidXNlcl9pZCI6MSwiZXhwIjoxNTYwMDgxMTQyLCJqdGkiOiI3ZTFmY2E1MTVjMmY0MmVkYTczZjExZDRjNTYzNDY3MSJ9.dVb8H-OgyvKf3UH3DOIzvcyZWAbYI5DntasCMT3cVRc'}
r = requests.get('http://127.0.0.1:8000/apis/apn',headers=headers)#, auth=('user', 'pass'))
print(r.headers['content-type'])
print(r.encoding)
print(r.status_code)
print(r.json())