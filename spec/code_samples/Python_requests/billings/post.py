import requests

url = "https://www.directfreight.com/api/billings"

payload = "{\"billing_address\":{},\"cc_data\":{},\"check_data\":{},\"promo_code\":\"<ADD STRING VALUE>\"}"
headers = {'end-user-token': 'SOME_STRING_VALUE'}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)