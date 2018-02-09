import requests

url = "https://www.directfreight.com/api/profiles/optins"

response = requests.request("POST", url)

print(response.text)