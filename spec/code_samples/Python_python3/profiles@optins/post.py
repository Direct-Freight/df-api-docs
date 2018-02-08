import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

conn.request("POST", "/api/profiles/optins")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))