import requests

url = "https://www.directfreight.com/api/profiles/documents"

headers = {'end-user-token': 'SOME_STRING_VALUE'}

response = requests.request("GET", url, headers=headers)

print(response.text)