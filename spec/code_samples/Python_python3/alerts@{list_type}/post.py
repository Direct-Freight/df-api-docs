import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

payload = "{\"days_of_week\":{},\"email_address\":\"<ADD STRING VALUE>\",\"end_hour\":{},\"expires_after\":{},\"list_order\":{},\"list_type\":{},\"minute_frequency\":{},\"send_type\":{},\"start_hour\":{},\"time_zone\":{}}"

conn.request("POST", "/api/alerts/%7Blist_type%7D", payload)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))