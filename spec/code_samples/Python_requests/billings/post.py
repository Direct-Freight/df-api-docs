import requests

url = "https://www.directfreight.com/api/billings"

payload = "{\"billing_address\":{},\"cc_data\":{},\"check_data\":{},\"promo_code\":\"<ADD STRING VALUE>\"}"
response = requests.request("POST", url, data=payload)

print(response.text)