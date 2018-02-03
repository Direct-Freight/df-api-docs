import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

payload = "{\"body\":\"<ADD STRING VALUE>\",\"title\":\"<ADD STRING VALUE>\"}"

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'end-user-token': "SOME_STRING_VALUE"
    }

conn.request("PATCH", "/api/boards/notes", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))