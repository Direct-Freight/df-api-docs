import requests

url = "https://www.directfreight.com/api/boards/hidden_entries"

payload = "{\"entry_id\":[\"<ADD STRING VALUE>\"]}"
response = requests.request("PATCH", url, data=payload)

print(response.text)