import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("GET", "/api/end_user_authentications/passwords?email=SOME_STRING_VALUE", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))