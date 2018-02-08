import requests

url = "https://www.directfreight.com/api/boards/hidden_entries"

querystring = {"entry_id":"SOME_STRING_VALUE"}

response = requests.request("DELETE", url, params=querystring)

print(response.text)