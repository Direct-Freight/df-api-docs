import requests

url = "https://www.directfreight.com/api/postings/%7Blist_type%7D/%7Baction%7D"

payload = "{\"source_id\":{},\"source_posting\":\"<ADD STRING VALUE>\"}"
response = requests.request("POST", url, data=payload)

print(response.text)