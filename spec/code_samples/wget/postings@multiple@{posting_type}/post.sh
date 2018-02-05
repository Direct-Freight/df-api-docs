wget --quiet \
  --method POST \
  --header 'end-user-token: SOME_STRING_VALUE' \
  --body-data '{"contact_fax":"<ADD STRING VALUE>","contact_name":"<ADD STRING VALUE>","contact_phone":"<ADD STRING VALUE>","delete_current_before_posting":false,"list":["<ADD STRING VALUE>"]}' \
  --output-document \
  - https://www.directfreight.com/api/postings/multiple/%7Bposting_type%7D