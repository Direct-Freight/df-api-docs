wget --quiet \
  --method PATCH \
  --header 'end-user-token: SOME_STRING_VALUE' \
  --body-data '{"current_name":"<ADD STRING VALUE>","new_name":"<ADD STRING VALUE>"}' \
  --output-document \
  - https://www.directfreight.com/api/profiles/documents