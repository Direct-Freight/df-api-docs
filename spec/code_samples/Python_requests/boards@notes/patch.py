import requests

url = "https://www.directfreight.com/api/boards/notes"

payload = "{\"body\":\"<ADD STRING VALUE>\",\"title\":\"<ADD STRING VALUE>\"}"
response = requests.request("PATCH", url, data=payload)

print(response.text)