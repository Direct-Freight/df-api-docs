import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

headers = { 'end-user-token': "SOME_STRING_VALUE" }

conn.request("DELETE", "/api/postings/custom_categories/%7Bcategory_type%7D?category_id=SOME_ARRAY_VALUE", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))