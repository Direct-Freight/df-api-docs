import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

payload = "{\"days_of_week\":{},\"email_address\":\"<ADD STRING VALUE>\",\"end_hour\":{},\"expires_after\":{},\"list_order\":{},\"list_type\":{},\"minute_frequency\":{},\"send_type\":{},\"start_hour\":{},\"time_zone\":{},\"search\":{\"search_id\":0,\"search_type\":\"<ADD STRING VALUE>\",\"date_received\":\"<ADD STRING VALUE>\",\"trailers\":\"<ADD STRING VALUE>\",\"date_available\":\"<ADD STRING VALUE>\",\"origin_state\":\"<ADD STRING VALUE>\",\"origin_city\":\"<ADD STRING VALUE>\",\"origin_radius\":0,\"destination_state\":\"<ADD STRING VALUE>\",\"destination_city\":\"<ADD STRING VALUE>\",\"destination_radius\":0,\"load_size\":\"<ADD STRING VALUE>\"}}"

conn.request("POST", "/api/alerts/%7Blist_type%7D", payload)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))