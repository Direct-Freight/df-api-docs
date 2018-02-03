import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

payload = "{\"source_id\":{},\"source_posting\":\"<ADD STRING VALUE>\"}"

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'end-user-token': "SOME_STRING_VALUE"
    }

conn.request("POST", "/api/postings/%7Bposting_type%7D/%7Baction%7D", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))