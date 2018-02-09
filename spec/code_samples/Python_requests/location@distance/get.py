import requests

url = "https://www.directfreight.com/api/location/distance"

querystring = {"origin_city":"SOME_STRING_VALUE","origin_state":"SOME_STRING_VALUE","destination_city":"SOME_STRING_VALUE","destination_state":"SOME_STRING_VALUE"}

response = requests.request("GET", url, params=querystring)

print(response.text)