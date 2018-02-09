import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

payload = "{\"source_id\":{},\"source_posting\":\"<ADD STRING VALUE>\"}"

conn.request("POST", "/api/postings/%7Blist_type%7D/%7Baction%7D", payload)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))