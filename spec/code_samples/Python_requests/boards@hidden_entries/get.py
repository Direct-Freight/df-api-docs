import requests

url = "https://www.directfreight.com/api/boards/hidden_entries"

querystring = {"entry_id":"SOME_ARRAY_VALUE"}

response = requests.request("GET", url, params=querystring)

print(response.text)