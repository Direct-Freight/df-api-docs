import requests

url = "https://www.directfreight.com/api/end_user_authentications"

querystring = {"":"SOME_STRING_VALUE"}

payload = "{\"login\":\"<ADD STRING VALUE>\",\"realm\":\"<ADD STRING VALUE>\",\"secret\":\"<ADD STRING VALUE>\"}"
headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)