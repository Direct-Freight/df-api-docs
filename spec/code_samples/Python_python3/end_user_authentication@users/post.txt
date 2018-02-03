import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

payload = "{\"email\":\"<ADD STRING VALUE>\",\"end-user-token\":\"<ADD STRING VALUE>\",\"password\":\"<ADD STRING VALUE>\"}"

headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("POST", "/api/end_user_authentication/users", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))