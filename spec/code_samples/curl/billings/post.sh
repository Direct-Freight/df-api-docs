curl --request POST \
  --url https://www.directfreight.com/api/billings \
  --header 'end-user-token: SOME_STRING_VALUE' \
  --data '{"billing_address":{},"cc_data":{},"check_data":{},"promo_code":"<ADD STRING VALUE>"}'