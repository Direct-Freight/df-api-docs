import requests

url = "https://www.directfreight.com/api/boards/notes"

querystring = {"entry_id":"SOME_ARRAY_VALUE"}

response = requests.request("GET", url, params=querystring)

print(response.text)