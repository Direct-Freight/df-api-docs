import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

conn.request("GET", "/api/locations/closest_city?latitude=SOME_NUMBER_VALUE&longitude=SOME_NUMBER_VALUE")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))