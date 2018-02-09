import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

payload = "{\"login\":\"<ADD STRING VALUE>\",\"realm\":\"username\",\"secret\":\"<ADD STRING VALUE>\"}"

conn.request("POST", "/api/end_user_authentications", payload)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))