import requests

url = "https://www.directfreight.com/api/boards/notes"

payload = "{\"body\":\"<ADD STRING VALUE>\",\"title\":\"<ADD STRING VALUE>\"}"
headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'end-user-token': "SOME_STRING_VALUE"
    }

response = requests.request("PATCH", url, data=payload, headers=headers)

print(response.text)