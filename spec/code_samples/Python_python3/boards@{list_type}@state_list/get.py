import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

conn.request("GET", "/api/boards/%7Blist_type%7D/state_list")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))