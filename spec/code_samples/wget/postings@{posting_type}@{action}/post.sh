wget --quiet \
  --method POST \
  --header 'end-user-token: SOME_STRING_VALUE' \
  --body-data '{"source_id":{},"source_posting":"<ADD STRING VALUE>"}' \
  --output-document \
  - https://www.directfreight.com/api/postings/%7Bposting_type%7D/%7Baction%7D