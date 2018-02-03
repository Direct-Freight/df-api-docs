import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("GET", "/api/boards/%7Bboard_type%7D/state_list", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))