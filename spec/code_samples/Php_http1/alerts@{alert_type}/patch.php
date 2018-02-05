<?php

HttpRequest::methodRegister('PATCH');
$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/alerts/%7Balert_type%7D');
$request->setMethod(HttpRequest::HTTP_METH_PATCH);

$request->setQueryData(array(
  'alert_id' => 'SOME_STRING_VALUE'
));

$request->setHeaders(array(
  'end-user-token' => 'SOME_STRING_VALUE'
));

$request->setBody('{"days_of_week":{},"end_hour":{},"expires_after":{},"list_order":{},"list_type":{},"minute_frequency":{},"send_type":{},"start_hour":{},"time_zone":{}}');

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}