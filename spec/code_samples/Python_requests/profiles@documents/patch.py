import requests

url = "https://www.directfreight.com/api/profiles/documents"

payload = "{\"current_name\":\"<ADD STRING VALUE>\",\"new_name\":\"<ADD STRING VALUE>\"}"
response = requests.request("PATCH", url, data=payload)

print(response.text)