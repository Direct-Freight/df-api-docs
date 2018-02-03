import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'end-user-token': "SOME_STRING_VALUE"
    }

conn.request("GET", "/api/credit_reports?credit_report_id=SOME_STRING_VALUE&format=SOME_STRING_VALUE", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))