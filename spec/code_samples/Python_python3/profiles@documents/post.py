import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

payload = "{\"The\":{}}"

conn.request("POST", "/api/profiles/documents", payload)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))