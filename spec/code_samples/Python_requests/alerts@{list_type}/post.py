import requests

url = "https://www.directfreight.com/api/alerts/%7Blist_type%7D"

payload = "{\"days_of_week\":{},\"email_address\":\"<ADD STRING VALUE>\",\"end_hour\":{},\"expires_after\":{},\"list_order\":{},\"list_type\":{},\"minute_frequency\":{},\"send_type\":{},\"start_hour\":{},\"time_zone\":{}}"
response = requests.request("POST", url, data=payload)

print(response.text)