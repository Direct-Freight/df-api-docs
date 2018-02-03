import requests

url = "https://www.directfreight.com/api/boards/%7Bboard_type%7D/state_list"

headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)