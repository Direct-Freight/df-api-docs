import requests

url = "https://www.directfreight.com/api/boards/%7Bboard_type%7D/state_list"

response = requests.request("GET", url)

print(response.text)