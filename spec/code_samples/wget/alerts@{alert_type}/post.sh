wget --quiet \
  --method POST \
  --header 'end-user-token: SOME_STRING_VALUE' \
  --body-data '{"days_of_week":{},"email_address":"<ADD STRING VALUE>","end_hour":{},"expires_after":{},"list_order":{},"list_type":{},"minute_frequency":{},"send_type":{},"start_hour":{},"time_zone":{}}' \
  --output-document \
  - https://www.directfreight.com/api/alerts/%7Balert_type%7D