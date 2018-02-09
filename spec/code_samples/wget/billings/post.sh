wget --quiet \
  --method POST \
  --body-data '{"billing_address":{},"cc_data":{},"check_data":{},"promo_code":"<ADD STRING VALUE>"}' \
  --output-document \
  - https://www.directfreight.com/api/billings