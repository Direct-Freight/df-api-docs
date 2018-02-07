wget --quiet \
  --method DELETE \
  --header 'end-user-token: SOME_STRING_VALUE' \
  --output-document \
  - 'https://www.directfreight.com/api/boards/notes?note_id=SOME_STRING_VALUE'