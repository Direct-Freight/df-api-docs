import requests

url = "https://www.directfreight.com/api/boards/hidden_entries"

response = requests.request("POST", url)

print(response.text)