import requests

url = "https://www.directfreight.com/api/profiles/mobile_carriers"

payload = "{\"carrier_id\":0}"
headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)