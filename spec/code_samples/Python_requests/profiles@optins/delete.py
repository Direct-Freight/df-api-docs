import requests

url = "https://www.directfreight.com/api/profiles/optins"

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'end-user-token': "SOME_STRING_VALUE"
    }

response = requests.request("DELETE", url, headers=headers)

print(response.text)