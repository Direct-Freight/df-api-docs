import requests

url = "https://www.directfreight.com/api/postings/%7Bposting_type%7D"

payload = "{\"comment\":{},\"custom_id\":{},\"destination_city\":{},\"destination_state\":{},\"height\":{},\"length\":{},\"load_size\":{},\"origin_city\":{},\"origin_state\":{},\"other_trailer_types\":{},\"pay_rate\":{},\"posting_id\":0,\"receive_date\":{},\"ship_date\":{},\"trailer_type\":{},\"weight\":{},\"width\":{}}"
response = requests.request("PATCH", url, data=payload)

print(response.text)