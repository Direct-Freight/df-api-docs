import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

conn.request("GET", "/api/end_user_authentications/passwords?email=SOME_STRING_VALUE")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))