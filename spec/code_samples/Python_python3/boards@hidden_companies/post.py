import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

payload = "{\"company_name\":\"<ADD STRING VALUE>\"}"

conn.request("POST", "/api/boards/hidden_companies", payload)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))