import requests

url = "https://www.directfreight.com/api/end_user_authentications/passwords"

querystring = {"email":"SOME_STRING_VALUE"}

response = requests.request("GET", url, params=querystring)

print(response.text)