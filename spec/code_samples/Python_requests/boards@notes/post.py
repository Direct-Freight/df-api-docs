import requests

url = "https://www.directfreight.com/api/boards/notes"

payload = "{\"body\":\"<ADD STRING VALUE>\",\"entry_id\":0,\"title\":\"<ADD STRING VALUE>\"}"
response = requests.request("POST", url, data=payload)

print(response.text)