import requests

url = "https://www.directfreight.com/api/end_user_authentications/dates"

response = requests.request("GET", url)

print(response.text)