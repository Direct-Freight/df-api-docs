curl --request PATCH \
  --url https://www.directfreight.com/api/boards/notes \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header 'end-user-token: SOME_STRING_VALUE' \
  --data '{"body":"<ADD STRING VALUE>","title":"<ADD STRING VALUE>"}'