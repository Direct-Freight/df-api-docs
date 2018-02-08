import requests

url = "https://www.directfreight.com/api/end_user_authentications"

response = requests.request("GET", url)

print(response.text)