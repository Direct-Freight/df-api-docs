import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

payload = "{\"entry_id\":[\"<ADD STRING VALUE>\"]}"

conn.request("PATCH", "/api/boards/hidden_entries", payload)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))