import requests

url = "https://www.directfreight.com/api/billings"

querystring = {"promo_code":"SOME_STRING_VALUE"}

response = requests.request("GET", url, params=querystring)

print(response.text)