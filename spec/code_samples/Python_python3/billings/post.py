import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

payload = "{\"billing_address\":{},\"cc_data\":{},\"check_data\":{},\"promo_code\":\"<ADD STRING VALUE>\"}"

conn.request("POST", "/api/billings", payload)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))