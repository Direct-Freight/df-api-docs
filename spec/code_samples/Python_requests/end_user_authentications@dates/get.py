import requests

url = "https://www.directfreight.com/api/end_user_authentications/dates"

headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)