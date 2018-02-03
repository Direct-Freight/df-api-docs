import requests

url = "https://www.directfreight.com/api/boards/%7Bboard_type%7D"

response = requests.request("PARAMETERS", url)

print(response.text)