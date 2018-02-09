import requests

url = "https://www.directfreight.com/api/profiles/mobile_carriers"

payload = "{\"carrier_id\":0}"
response = requests.request("GET", url, data=payload)

print(response.text)