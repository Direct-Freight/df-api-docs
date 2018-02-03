import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'end-user-token': "SOME_STRING_VALUE"
    }

conn.request("POST", "/api/postings/custom_categories/%7Bcategory_type%7D", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))