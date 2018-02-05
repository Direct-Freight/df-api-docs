wget --quiet \
  --method DELETE \
  --header 'end-user-token: SOME_STRING_VALUE' \
  --output-document \
  - 'https://www.directfreight.com/api/end_user_authentications?=SOME_STRING_VALUE'