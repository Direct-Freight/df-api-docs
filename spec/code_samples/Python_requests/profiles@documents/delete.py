import requests

url = "https://www.directfreight.com/api/profiles/documents"

response = requests.request("DELETE", url)

print(response.text)