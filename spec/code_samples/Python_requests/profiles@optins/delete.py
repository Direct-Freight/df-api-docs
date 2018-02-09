import requests

url = "https://www.directfreight.com/api/profiles/optins"

response = requests.request("DELETE", url)

print(response.text)