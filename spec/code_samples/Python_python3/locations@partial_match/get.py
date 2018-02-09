import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

conn.request("GET", "/api/locations/partial_match?term=SOME_STRING_VALUE&search_type=SOME_STRING_VALUE")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))