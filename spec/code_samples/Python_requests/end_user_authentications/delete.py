import requests

url = "https://www.directfreight.com/api/end_user_authentications"

response = requests.request("DELETE", url)

print(response.text)