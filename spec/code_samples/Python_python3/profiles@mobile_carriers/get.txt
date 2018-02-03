import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

payload = "{\"carrier_id\":0}"

headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("GET", "/api/profiles/mobile_carriers", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))