import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

payload = "{\"contact_fax\":\"<ADD STRING VALUE>\",\"contact_name\":\"<ADD STRING VALUE>\",\"contact_phone\":\"<ADD STRING VALUE>\",\"delete_current_before_posting\":false,\"list\":[\"<ADD STRING VALUE>\"]}"

headers = { 'end-user-token': "SOME_STRING_VALUE" }

conn.request("POST", "/api/postings/multiple/%7Bposting_type%7D", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))