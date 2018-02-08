import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

payload = "{\"current_name\":\"<ADD STRING VALUE>\",\"new_name\":\"<ADD STRING VALUE>\"}"

conn.request("PATCH", "/api/profiles/documents", payload)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))