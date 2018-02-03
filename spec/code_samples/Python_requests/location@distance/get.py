import requests

url = "https://www.directfreight.com/api/location/distance"

querystring = {"origin_city":"SOME_STRING_VALUE","origin_state":"SOME_STRING_VALUE","destination_city":"SOME_STRING_VALUE","destination_state":"SOME_STRING_VALUE"}

headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)