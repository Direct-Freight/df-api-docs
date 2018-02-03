import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

payload = "{\"The\":{}}"

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'end-user-token': "SOME_STRING_VALUE"
    }

conn.request("POST", "/api/profiles/documents", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))