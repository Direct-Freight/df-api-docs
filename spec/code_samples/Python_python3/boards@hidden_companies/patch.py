import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

payload = "{\"company_id\":\"<ADD STRING VALUE>\"}"

headers = { 'end-user-token': "SOME_STRING_VALUE" }

conn.request("PATCH", "/api/boards/hidden_companies", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))