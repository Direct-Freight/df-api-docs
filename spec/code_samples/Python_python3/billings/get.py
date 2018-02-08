import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

conn.request("GET", "/api/billings?promo_code=SOME_STRING_VALUE")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))