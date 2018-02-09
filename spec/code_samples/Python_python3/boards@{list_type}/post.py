import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

payload = "{\"alert_id\":0,\"count\":false,\"sort_parameter\":\"<ADD STRING VALUE>\",\"item_count\":0,\"page_number\":0,\"origin_city\":\"<ADD STRING VALUE>\",\"origin_radius\":0,\"origin_state\":\"<ADD STRING VALUE>\",\"destination_city\":\"<ADD STRING VALUE>\",\"destination_radius\":0,\"destination_state\":[\"<ADD STRING VALUE>\"],\"load_size\":\"Full\",\"only_new\":false,\"ship_date\":[\"<ADD STRING VALUE>\"],\"trailer_type\":[\"<ADD STRING VALUE>\"]}"

conn.request("POST", "/api/boards/%7Blist_type%7D", payload)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))