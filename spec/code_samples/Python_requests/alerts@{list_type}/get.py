import requests

url = "https://www.directfreight.com/api/alerts/%7Blist_type%7D"

querystring = {"alert_id":"SOME_ARRAY_VALUE"}

response = requests.request("GET", url, params=querystring)

print(response.text)