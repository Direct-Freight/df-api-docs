import requests

url = "https://www.directfreight.com/api/boards/hidden_entries"

querystring = {"entry_id":"SOME_ARRAY_VALUE"}

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'end-user-token': "SOME_STRING_VALUE"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)