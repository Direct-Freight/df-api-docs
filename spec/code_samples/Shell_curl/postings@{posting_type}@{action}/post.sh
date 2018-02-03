curl --request POST \
  --url https://www.directfreight.com/api/postings/%7Bposting_type%7D/%7Baction%7D \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header 'end-user-token: SOME_STRING_VALUE' \
  --data '{"source_id":{},"source_posting":"<ADD STRING VALUE>"}'