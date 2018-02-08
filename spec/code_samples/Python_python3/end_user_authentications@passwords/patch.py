import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

payload = "{\"new_password\":\"<ADD STRING VALUE>\",\"old_password\":\"<ADD STRING VALUE>\"}"

conn.request("PATCH", "/api/end_user_authentications/passwords", payload)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))