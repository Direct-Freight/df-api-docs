import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

conn.request("GET", "/api/location/distance?origin_city=SOME_STRING_VALUE&origin_state=SOME_STRING_VALUE&destination_city=SOME_STRING_VALUE&destination_state=SOME_STRING_VALUE")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))