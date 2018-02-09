import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

payload = "{\"body\":\"<ADD STRING VALUE>\",\"title\":\"<ADD STRING VALUE>\"}"

conn.request("PATCH", "/api/boards/notes", payload)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))