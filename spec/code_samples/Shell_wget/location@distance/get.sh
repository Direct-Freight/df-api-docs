wget --quiet \
  --method GET \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --output-document \
  - 'https://www.directfreight.com/api/location/distance?origin_city=SOME_STRING_VALUE&origin_state=SOME_STRING_VALUE&destination_city=SOME_STRING_VALUE&destination_state=SOME_STRING_VALUE'