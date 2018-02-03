wget --quiet \
  --method GET \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --output-document \
  - 'https://www.directfreight.com/api/end_user_authentications/passwords?email=SOME_STRING_VALUE'