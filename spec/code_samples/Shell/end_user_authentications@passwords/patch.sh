curl --request PATCH \
  --url https://www.directfreight.com/api/end_user_authentications/passwords \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header 'end-user-token: SOME_STRING_VALUE' \
  --data '{"new_password":"<ADD STRING VALUE>","old_password":"<ADD STRING VALUE>"}'