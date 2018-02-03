wget --quiet \
  --method POST \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header 'end-user-token: SOME_STRING_VALUE' \
  --body-data '{"body":"<ADD STRING VALUE>","entry_id":0,"title":"<ADD STRING VALUE>"}' \
  --output-document \
  - https://www.directfreight.com/api/boards/notes