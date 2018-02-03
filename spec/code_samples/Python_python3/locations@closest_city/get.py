import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("GET", "/api/locations/closest_city?latitude=SOME_NUMBER_VALUE&longitude=SOME_NUMBER_VALUE", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))