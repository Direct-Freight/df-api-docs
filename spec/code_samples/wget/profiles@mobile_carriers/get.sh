wget --quiet \
  --method GET \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --body-data '{"carrier_id":0}' \
  --output-document \
  - https://www.directfreight.com/api/profiles/mobile_carriers