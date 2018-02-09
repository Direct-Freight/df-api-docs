import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

conn.request("DELETE", "/api/end_user_authentications")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))