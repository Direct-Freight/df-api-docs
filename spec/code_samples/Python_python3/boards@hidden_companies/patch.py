import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

payload = "{\"company_id\":\"<ADD STRING VALUE>\"}"

conn.request("PATCH", "/api/boards/hidden_companies", payload)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))