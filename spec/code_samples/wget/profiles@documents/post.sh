wget --quiet \
  --method POST \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header 'end-user-token: SOME_STRING_VALUE' \
  --body-data '{"The":{}}' \
  --output-document \
  - https://www.directfreight.com/api/profiles/documents