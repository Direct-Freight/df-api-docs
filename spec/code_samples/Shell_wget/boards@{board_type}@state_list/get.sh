wget --quiet \
  --method GET \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --output-document \
  - https://www.directfreight.com/api/boards/%7Bboard_type%7D/state_list