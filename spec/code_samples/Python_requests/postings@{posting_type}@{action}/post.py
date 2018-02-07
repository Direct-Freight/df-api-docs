import requests

url = "https://www.directfreight.com/api/postings/%7Bposting_type%7D/%7Baction%7D"

payload = "{\"source_id\":{},\"source_posting\":\"<ADD STRING VALUE>\"}"
headers = {'end-user-token': 'SOME_STRING_VALUE'}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)