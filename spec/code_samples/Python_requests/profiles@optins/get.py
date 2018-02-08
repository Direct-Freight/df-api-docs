import requests

url = "https://www.directfreight.com/api/profiles/optins"

response = requests.request("GET", url)

print(response.text)