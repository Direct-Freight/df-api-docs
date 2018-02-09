import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

payload = "{\"carrier_id\":0}"

conn.request("GET", "/api/profiles/mobile_carriers", payload)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))