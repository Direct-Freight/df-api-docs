import requests

url = "https://www.directfreight.com/api/end_user_authentications"

payload = "{\"login\":\"<ADD STRING VALUE>\",\"realm\":\"username\",\"secret\":\"<ADD STRING VALUE>\"}"
response = requests.request("POST", url, data=payload)

print(response.text)