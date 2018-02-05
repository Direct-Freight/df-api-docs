import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

headers = { 'end-user-token': "SOME_STRING_VALUE" }

conn.request("GET", "/api/alerts/%7Balert_type%7D?alert_id=SOME_ARRAY_VALUE", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))