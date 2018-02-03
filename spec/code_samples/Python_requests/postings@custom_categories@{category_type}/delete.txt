import requests

url = "https://www.directfreight.com/api/postings/custom_categories/%7Bcategory_type%7D"

querystring = {"category_id":"SOME_ARRAY_VALUE"}

headers = {'end-user-token': 'SOME_STRING_VALUE'}

response = requests.request("DELETE", url, headers=headers, params=querystring)

print(response.text)