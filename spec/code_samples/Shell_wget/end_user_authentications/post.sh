wget --quiet \
  --method POST \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --body-data '{"login":"<ADD STRING VALUE>","realm":"<ADD STRING VALUE>","secret":"<ADD STRING VALUE>"}' \
  --output-document \
  - 'https://www.directfreight.com/api/end_user_authentications?=SOME_STRING_VALUE'