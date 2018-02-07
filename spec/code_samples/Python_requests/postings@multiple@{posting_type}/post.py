import requests

url = "https://www.directfreight.com/api/postings/multiple/%7Bposting_type%7D"

payload = "{\"contact_fax\":\"<ADD STRING VALUE>\",\"contact_name\":\"<ADD STRING VALUE>\",\"contact_phone\":\"<ADD STRING VALUE>\",\"delete_current_before_posting\":false,\"list\":[\"<ADD STRING VALUE>\"]}"
headers = {'end-user-token': 'SOME_STRING_VALUE'}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)