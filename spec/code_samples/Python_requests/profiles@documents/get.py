import requests

url = "https://www.directfreight.com/api/profiles/documents"

response = requests.request("GET", url)

print(response.text)