import requests

url = "https://www.directfreight.com/api/profiles/documents"

payload = "{\"current_name\":\"<ADD STRING VALUE>\",\"new_name\":\"<ADD STRING VALUE>\"}"
headers = {'end-user-token': 'SOME_STRING_VALUE'}

response = requests.request("PATCH", url, data=payload, headers=headers)

print(response.text)