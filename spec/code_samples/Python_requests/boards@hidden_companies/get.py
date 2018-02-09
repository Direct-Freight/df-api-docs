import requests

url = "https://www.directfreight.com/api/boards/hidden_companies"

querystring = {"company_name":"SOME_ARRAY_VALUE"}

response = requests.request("GET", url, params=querystring)

print(response.text)