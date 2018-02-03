wget --quiet \
  --method GET \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --output-document \
  - 'https://www.directfreight.com/api/locations/closest_city?latitude=SOME_NUMBER_VALUE&longitude=SOME_NUMBER_VALUE'