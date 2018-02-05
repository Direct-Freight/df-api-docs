wget --quiet \
  --method GET \
  --header 'end-user-token: SOME_STRING_VALUE' \
  --output-document \
  - 'https://www.directfreight.com/api/billings?promo_code=SOME_STRING_VALUE'