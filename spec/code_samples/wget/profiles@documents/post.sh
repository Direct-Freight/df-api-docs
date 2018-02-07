wget --quiet \
  --method POST \
  --header 'end-user-token: SOME_STRING_VALUE' \
  --body-data '{"The":{}}' \
  --output-document \
  - https://www.directfreight.com/api/profiles/documents