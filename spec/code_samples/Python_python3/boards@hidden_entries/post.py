import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

conn.request("POST", "/api/boards/hidden_entries")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))