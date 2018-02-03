wget --quiet \
  --method PATCH \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header 'end-user-token: SOME_STRING_VALUE' \
  --body-data '{"company_id":"<ADD STRING VALUE>"}' \
  --output-document \
  - https://www.directfreight.com/api/boards/hidden_companies