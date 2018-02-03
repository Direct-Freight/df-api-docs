import requests

url = "https://www.directfreight.com/api/locations/closest_city"

querystring = {"latitude":"SOME_NUMBER_VALUE","longitude":"SOME_NUMBER_VALUE"}

headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)