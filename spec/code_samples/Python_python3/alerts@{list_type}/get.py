import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

conn.request("GET", "/api/alerts/%7Blist_type%7D?alert_id=SOME_ARRAY_VALUE")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))