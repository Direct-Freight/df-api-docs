wget --quiet \
  --method GET \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --output-document \
  - 'https://www.directfreight.com/api/locations/partial_match?term=SOME_STRING_VALUE&search_type=SOME_STRING_VALUE'