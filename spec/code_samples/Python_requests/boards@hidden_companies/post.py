import requests

url = "https://www.directfreight.com/api/boards/hidden_companies"

payload = "{\"company_name\":\"<ADD STRING VALUE>\"}"
response = requests.request("POST", url, data=payload)

print(response.text)