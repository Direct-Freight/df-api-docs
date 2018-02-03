wget --quiet \
  --method PATCH \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header 'end-user-token: SOME_STRING_VALUE' \
  --body-data '{"new_password":"<ADD STRING VALUE>","old_password":"<ADD STRING VALUE>"}' \
  --output-document \
  - https://www.directfreight.com/api/end_user_authentications/passwords