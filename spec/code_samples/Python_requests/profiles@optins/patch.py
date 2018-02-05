import requests

url = "https://www.directfreight.com/api/profiles/optins"

headers = {'end-user-token': 'SOME_STRING_VALUE'}

response = requests.request("PATCH", url, headers=headers)

print(response.text)