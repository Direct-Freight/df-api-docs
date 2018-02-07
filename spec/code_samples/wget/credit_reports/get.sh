wget --quiet \
  --method GET \
  --header 'end-user-token: SOME_STRING_VALUE' \
  --output-document \
  - 'https://www.directfreight.com/api/credit_reports?credit_report_id=SOME_STRING_VALUE&format=SOME_STRING_VALUE'