import requests

url = "https://www.directfreight.com/api/boards/hidden_companies"

payload = "{\"company_name\":\"<ADD STRING VALUE>\"}"
headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'end-user-token': "SOME_STRING_VALUE"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)