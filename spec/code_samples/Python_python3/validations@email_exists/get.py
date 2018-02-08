import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

conn.request("GET", "/api/validations/email_exists?email=SOME_STRING_VALUE")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))