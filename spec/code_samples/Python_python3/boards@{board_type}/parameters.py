import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

conn.request("PARAMETERS", "/api/boards/%7Bboard_type%7D")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))