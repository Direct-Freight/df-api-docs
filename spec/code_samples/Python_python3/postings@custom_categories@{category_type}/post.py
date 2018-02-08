import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

conn.request("POST", "/api/postings/custom_categories/%7Bcategory_type%7D")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))