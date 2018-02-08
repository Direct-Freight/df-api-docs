wget --quiet \
  --method PATCH \
  --body-data '{"new_password":"<ADD STRING VALUE>","old_password":"<ADD STRING VALUE>"}' \
  --output-document \
  - https://www.directfreight.com/api/end_user_authentications/passwords