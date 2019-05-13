import http.client

h = http.client.HTTPConnection("192.168.110.116:8080")
h.request("GET", "/")
data = h.getresponse()
print (data.code)
print (data.headers)
text = data.readlines()
for t in text:
    print(t.decode('utf-8'))

