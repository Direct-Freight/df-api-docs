import requests

url = "https://www.directfreight.com/api/boards/hidden_entries"

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'end-user-token': "SOME_STRING_VALUE"
    }

response = requests.request("POST", url, headers=headers)

print(response.text)