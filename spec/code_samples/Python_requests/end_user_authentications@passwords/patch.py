import requests

url = "https://www.directfreight.com/api/end_user_authentications/passwords"

payload = "{\"new_password\":\"<ADD STRING VALUE>\",\"old_password\":\"<ADD STRING VALUE>\"}"
response = requests.request("PATCH", url, data=payload)

print(response.text)