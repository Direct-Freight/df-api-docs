import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

conn.request("PATCH", "/api/profiles/optins")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))