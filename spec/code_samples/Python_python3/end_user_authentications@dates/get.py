import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

conn.request("GET", "/api/end_user_authentications/dates")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))