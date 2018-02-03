import requests

url = "https://www.directfreight.com/api/alerts/%7Balert_type%7D"

querystring = {"alert_id":"SOME_ARRAY_VALUE"}

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'end-user-token': "SOME_STRING_VALUE"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)