import requests

url = "https://www.directfreight.com/api/postings/multiple/%7Blist_type%7D"

payload = "{\"contact_fax\":\"<ADD STRING VALUE>\",\"contact_name\":\"<ADD STRING VALUE>\",\"contact_phone\":\"<ADD STRING VALUE>\",\"delete_current_before_posting\":false,\"list\":[\"<ADD STRING VALUE>\"]}"
response = requests.request("POST", url, data=payload)

print(response.text)