import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'end-user-token': "SOME_STRING_VALUE"
    }

conn.request("DELETE", "/api/postings/%7Bposting_type%7D?posting_id=SOME_ARRAY_VALUE", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))