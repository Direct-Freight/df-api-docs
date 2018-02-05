import requests

url = "https://www.directfreight.com/api/end_user_authentications"

querystring = {"":"SOME_STRING_VALUE"}

payload = "{\"login\":\"<ADD STRING VALUE>\",\"realm\":\"<ADD STRING VALUE>\",\"secret\":\"<ADD STRING VALUE>\"}"
response = requests.request("POST", url, data=payload, params=querystring)

print(response.text)