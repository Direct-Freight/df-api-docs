import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

payload = "{\"email\":\"<ADD STRING VALUE>\",\"password\":\"<ADD STRING VALUE>\"}"

conn.request("POST", "/api/end_user_authentication/users", payload)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))