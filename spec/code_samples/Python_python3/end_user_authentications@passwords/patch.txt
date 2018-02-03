import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

payload = "{\"new_password\":\"<ADD STRING VALUE>\",\"old_password\":\"<ADD STRING VALUE>\"}"

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'end-user-token': "SOME_STRING_VALUE"
    }

conn.request("PATCH", "/api/end_user_authentications/passwords", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))