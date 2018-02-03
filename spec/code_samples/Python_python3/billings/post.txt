import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

payload = "{\"billing_address\":{},\"cc_data\":{},\"check_data\":{},\"promo_code\":\"<ADD STRING VALUE>\"}"

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'end-user-token': "SOME_STRING_VALUE"
    }

conn.request("POST", "/api/billings", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))