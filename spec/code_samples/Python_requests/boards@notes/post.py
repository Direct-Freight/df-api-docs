import requests

url = "https://www.directfreight.com/api/boards/notes"

payload = "{\"body\":\"<ADD STRING VALUE>\",\"entry_id\":0,\"title\":\"<ADD STRING VALUE>\"}"
headers = {'end-user-token': 'SOME_STRING_VALUE'}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)