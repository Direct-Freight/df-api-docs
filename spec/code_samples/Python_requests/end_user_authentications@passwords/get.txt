import requests

url = "https://www.directfreight.com/api/end_user_authentications/passwords"

querystring = {"email":"SOME_STRING_VALUE"}

headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)