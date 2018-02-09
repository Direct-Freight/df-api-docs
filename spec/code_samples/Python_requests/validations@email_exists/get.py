import requests

url = "https://www.directfreight.com/api/validations/email_exists"

querystring = {"email":"SOME_STRING_VALUE"}

response = requests.request("GET", url, params=querystring)

print(response.text)