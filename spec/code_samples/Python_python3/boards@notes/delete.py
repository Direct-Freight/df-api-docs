import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

conn.request("DELETE", "/api/boards/notes?note_id=SOME_STRING_VALUE")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))