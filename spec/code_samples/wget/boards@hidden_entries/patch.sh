wget --quiet \
  --method PATCH \
  --header 'end-user-token: SOME_STRING_VALUE' \
  --body-data '{"entry_id":["<ADD STRING VALUE>"]}' \
  --output-document \
  - https://www.directfreight.com/api/boards/hidden_entries