import requests

url = "https://www.directfreight.com/api/profiles"

response = requests.request("GET", url)

print(response.text)