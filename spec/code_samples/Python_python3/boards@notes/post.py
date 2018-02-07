import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

payload = "{\"body\":\"<ADD STRING VALUE>\",\"entry_id\":0,\"title\":\"<ADD STRING VALUE>\"}"

headers = { 'end-user-token': "SOME_STRING_VALUE" }

conn.request("POST", "/api/boards/notes", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))