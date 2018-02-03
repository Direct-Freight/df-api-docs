import requests

url = "https://www.directfreight.com/api/end_user_authentication/users"

payload = "{\"email\":\"<ADD STRING VALUE>\",\"end-user-token\":\"<ADD STRING VALUE>\",\"password\":\"<ADD STRING VALUE>\"}"
headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)