import requests

url = "https://www.directfreight.com/api/profiles/documents"

payload = "{\"current_name\":\"<ADD STRING VALUE>\",\"new_name\":\"<ADD STRING VALUE>\"}"
headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'end-user-token': "SOME_STRING_VALUE"
    }

response = requests.request("PATCH", url, data=payload, headers=headers)

print(response.text)