import requests

url = "https://www.directfreight.com/api/postings/custom_categories/%7Bcategory_type%7D"

response = requests.request("POST", url)

print(response.text)