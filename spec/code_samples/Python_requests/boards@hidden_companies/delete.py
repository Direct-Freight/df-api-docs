import requests

url = "https://www.directfreight.com/api/boards/hidden_companies"

querystring = {"company_id":"SOME_STRING_VALUE"}

headers = {'end-user-token': 'SOME_STRING_VALUE'}

response = requests.request("DELETE", url, headers=headers, params=querystring)

print(response.text)