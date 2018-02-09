import requests

url = "https://www.directfreight.com/api/locations/partial_match"

querystring = {"term":"SOME_STRING_VALUE","search_type":"SOME_STRING_VALUE"}

response = requests.request("GET", url, params=querystring)

print(response.text)