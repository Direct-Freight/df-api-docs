import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

conn.request("GET", "/api/credit_reports?credit_report_id=SOME_STRING_VALUE&format=SOME_STRING_VALUE")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))