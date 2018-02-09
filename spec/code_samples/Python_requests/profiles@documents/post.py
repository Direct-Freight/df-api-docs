import requests

url = "https://www.directfreight.com/api/profiles/documents"

payload = "{\"The\":{}}"
response = requests.request("POST", url, data=payload)

print(response.text)