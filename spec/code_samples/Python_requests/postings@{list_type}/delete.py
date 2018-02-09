import requests

url = "https://www.directfreight.com/api/postings/%7Blist_type%7D"

querystring = {"posting_id":"SOME_ARRAY_VALUE"}

response = requests.request("DELETE", url, params=querystring)

print(response.text)