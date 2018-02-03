wget --quiet \
  --method DELETE \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header 'end-user-token: SOME_STRING_VALUE' \
  --output-document \
  - 'https://www.directfreight.com/api/boards/notes?note_id=SOME_STRING_VALUE'