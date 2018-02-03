import requests

url = "https://www.directfreight.com/api/locations/partial_match"

querystring = {"term":"SOME_STRING_VALUE","search_type":"SOME_STRING_VALUE"}

headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)