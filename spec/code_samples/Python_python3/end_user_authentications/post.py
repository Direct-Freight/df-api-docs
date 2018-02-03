import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

payload = "{\"login\":\"<ADD STRING VALUE>\",\"realm\":\"<ADD STRING VALUE>\",\"secret\":\"<ADD STRING VALUE>\"}"

headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("POST", "/api/end_user_authentications?=SOME_STRING_VALUE", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))