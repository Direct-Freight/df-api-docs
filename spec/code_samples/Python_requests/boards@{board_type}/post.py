import requests

url = "https://www.directfreight.com/api/boards/%7Bboard_type%7D"

payload = "{\"alert_id\":5555,\"count\":false,\"destination_city\":\"chicago\",\"destination_radius\":0,\"destination_state\":[\"<ADD STRING VALUE>\"],\"item_count\":0,\"load_size\":\"Full\",\"only_new\":false,\"origin_city\":\"chillicothe\",\"origin_radius\":0,\"origin_state\":[\"<ADD STRING VALUE>\"],\"page_number\":0,\"ship_date\":[\"<ADD STRING VALUE>\"],\"total_items\":0,\"total_pages\":0,\"trailer_type\":[\"<ADD STRING VALUE>\"]}"
headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)