import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

conn.request("GET", "/api/postings/%7Bposting_type%7D?posting_id=SOME_ARRAY_VALUE")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))