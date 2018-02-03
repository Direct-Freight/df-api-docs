import http.client

conn = http.client.HTTPSConnection("www.directfreight.com")

payload = "{\"address\":\"<ADD STRING VALUE>\",\"city\":\"<ADD STRING VALUE>\",\"company\":\"<ADD STRING VALUE>\",\"contact_extension\":\"<ADD STRING VALUE>\",\"contact_name\":\"<ADD STRING VALUE>\",\"contact_number\":\"<ADD STRING VALUE>\",\"dot_number\":\"<ADD STRING VALUE>\",\"fax_number\":\"<ADD STRING VALUE>\",\"mc_number\":\"<ADD STRING VALUE>\",\"mobile_carrier\":0,\"mobile_number\":\"<ADD STRING VALUE>\",\"state\":\"<ADD STRING VALUE>\",\"web_page\":\"<ADD STRING VALUE>\",\"zip\":\"<ADD STRING VALUE>\"}"

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'end-user-token': "SOME_STRING_VALUE"
    }

conn.request("PATCH", "/api/profiles", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))