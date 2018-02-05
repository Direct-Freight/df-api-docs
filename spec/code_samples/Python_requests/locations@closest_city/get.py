import requests

url = "https://www.directfreight.com/api/locations/closest_city"

querystring = {"latitude":"SOME_NUMBER_VALUE","longitude":"SOME_NUMBER_VALUE"}

response = requests.request("GET", url, params=querystring)

print(response.text)