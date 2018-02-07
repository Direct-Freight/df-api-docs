wget --quiet \
  --method GET \
  --header 'end-user-token: SOME_STRING_VALUE' \
  --output-document \
  - 'https://www.directfreight.com/api/validations/email_exists?email=SOME_STRING_VALUE'