import requests

url = "https://www.directfreight.com/api/end_user_authentication/users"

payload = "{\"email\":\"<ADD STRING VALUE>\",\"end-user-token\":\"<ADD STRING VALUE>\",\"password\":\"<ADD STRING VALUE>\"}"
response = requests.request("POST", url, data=payload)

print(response.text)