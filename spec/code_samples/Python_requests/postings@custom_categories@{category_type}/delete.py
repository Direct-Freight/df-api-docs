import requests

url = "https://www.directfreight.com/api/postings/custom_categories/%7Bcategory_type%7D"

querystring = {"category_id":"SOME_ARRAY_VALUE"}

response = requests.request("DELETE", url, params=querystring)

print(response.text)