import requests

url = "https://www.directfreight.com/api/profiles/optins"

headers = {'end-user-token': 'SOME_STRING_VALUE'}

response = requests.request("POST", url, headers=headers)

print(response.text)