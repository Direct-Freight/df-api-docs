import requests

url = "https://www.directfreight.com/api/postings/%7Bposting_type%7D"

querystring = {"posting_id":"SOME_ARRAY_VALUE"}

headers = {'end-user-token': 'SOME_STRING_VALUE'}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)