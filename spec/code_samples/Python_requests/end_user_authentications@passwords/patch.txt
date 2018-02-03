import requests

url = "https://www.directfreight.com/api/end_user_authentications/passwords"

payload = "{\"new_password\":\"<ADD STRING VALUE>\",\"old_password\":\"<ADD STRING VALUE>\"}"
headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'end-user-token': "SOME_STRING_VALUE"
    }

response = requests.request("PATCH", url, data=payload, headers=headers)

print(response.text)