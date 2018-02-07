import requests

url = "https://www.directfreight.com/api/boards/hidden_companies"

payload = "{\"company_id\":\"<ADD STRING VALUE>\"}"
headers = {'end-user-token': 'SOME_STRING_VALUE'}

response = requests.request("PATCH", url, data=payload, headers=headers)

print(response.text)