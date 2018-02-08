import requests

url = "https://www.directfreight.com/api/alerts/%7Blist_type%7D"

querystring = {"alert_id":"SOME_STRING_VALUE"}

payload = "{\"days_of_week\":{},\"end_hour\":{},\"expires_after\":{},\"list_order\":{},\"list_type\":{},\"minute_frequency\":{},\"send_type\":{},\"start_hour\":{},\"time_zone\":{}}"
response = requests.request("PATCH", url, data=payload, params=querystring)

print(response.text)