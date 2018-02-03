import requests

url = "https://www.directfreight.com/api/boards/%7Bboard_type%7D/%7Borigin_state%7D/%7Borigin_city%7D/%7Borigin_radius%7D/%7Bload_type%7D/%7Bdestination_state%7D/%7Bdestination_city%7D"

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'end-user-token': "SOME_STRING_VALUE"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)