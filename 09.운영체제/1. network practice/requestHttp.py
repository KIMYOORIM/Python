import requests

baseUrl = 'http://192.168.110.116:8080'

r = requests.get(baseUrl)
print(r)
print(r.status_code)
