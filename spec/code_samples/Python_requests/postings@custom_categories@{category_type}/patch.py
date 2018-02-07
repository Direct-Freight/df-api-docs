import requests

url = "https://www.directfreight.com/api/postings/custom_categories/%7Bcategory_type%7D"

headers = {'end-user-token': 'SOME_STRING_VALUE'}

response = requests.request("PATCH", url, headers=headers)

print(response.text)