import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

conn.request("GET", "/api/boards/%7Bboard_type%7D/%7Borigin_state%7D/%7Borigin_city%7D/%7Borigin_radius%7D/%7Bload_type%7D/%7Bdestination_state%7D/%7Bdestination_city%7D")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))