import requests

url = "https://www.directfreight.com/api/profiles/optins"

response = requests.request("PATCH", url)

print(response.text)