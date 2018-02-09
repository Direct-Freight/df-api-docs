import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

conn.request("GET", "/api/boards/notes?entry_id=SOME_ARRAY_VALUE")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))