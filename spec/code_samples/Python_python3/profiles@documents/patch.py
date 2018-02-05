import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

payload = "{\"current_name\":\"<ADD STRING VALUE>\",\"new_name\":\"<ADD STRING VALUE>\"}"

headers = { 'end-user-token': "SOME_STRING_VALUE" }

conn.request("PATCH", "/api/profiles/documents", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))