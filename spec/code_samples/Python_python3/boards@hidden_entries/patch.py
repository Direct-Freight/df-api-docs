import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

payload = "{\"entry_id\":[\"<ADD STRING VALUE>\"]}"

headers = { 'end-user-token': "SOME_STRING_VALUE" }

conn.request("PATCH", "/api/boards/hidden_entries", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))