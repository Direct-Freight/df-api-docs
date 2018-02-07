wget --quiet \
  --method DELETE \
  --header 'end-user-token: SOME_STRING_VALUE' \
  --output-document \
  - 'https://www.directfreight.com/api/boards/hidden_companies?company_id=SOME_STRING_VALUE'