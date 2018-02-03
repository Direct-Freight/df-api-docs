import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

payload = "{\"days_of_week\":{},\"end_hour\":{},\"expires_after\":{},\"list_order\":{},\"list_type\":{},\"minute_frequency\":{},\"send_type\":{},\"start_hour\":{},\"time_zone\":{}}"

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'end-user-token': "SOME_STRING_VALUE"
    }

conn.request("PATCH", "/api/alerts/%7Balert_type%7D?alert_id=SOME_STRING_VALUE", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))