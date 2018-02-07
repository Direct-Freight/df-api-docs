curl --request PATCH \
  --url https://www.directfreight.com/api/end_user_authentications/passwords \
  --header 'end-user-token: SOME_STRING_VALUE' \
  --data '{"new_password":"<ADD STRING VALUE>","old_password":"<ADD STRING VALUE>"}'