import requests

url = "https://www.directfreight.com/api/validations/email_exists"

querystring = {"email":"SOME_STRING_VALUE"}

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'end-user-token': "SOME_STRING_VALUE"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)