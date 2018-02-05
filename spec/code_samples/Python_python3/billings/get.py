import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

headers = { 'end-user-token': "SOME_STRING_VALUE" }

conn.request("GET", "/api/billings?promo_code=SOME_STRING_VALUE", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))