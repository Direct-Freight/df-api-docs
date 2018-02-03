wget --quiet \
  --method POST \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --body-data '{"email":"<ADD STRING VALUE>","end-user-token":"<ADD STRING VALUE>","password":"<ADD STRING VALUE>"}' \
  --output-document \
  - https://www.directfreight.com/api/end_user_authentication/users