import requests

url = "https://www.directfreight.com/api/boards/hidden_entries"

payload = "{\"entry_id\":[\"<ADD STRING VALUE>\"]}"
headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'end-user-token': "SOME_STRING_VALUE"
    }

response = requests.request("PATCH", url, data=payload, headers=headers)

print(response.text)