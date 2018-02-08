import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

conn.request("GET", "/api/profiles")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))