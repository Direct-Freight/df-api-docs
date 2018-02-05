import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

headers = { 'end-user-token': "SOME_STRING_VALUE" }

conn.request("POST", "/api/boards/hidden_entries", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))