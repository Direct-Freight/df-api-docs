<?php

$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/alerts/%7Blist_type%7D');
$request->setMethod(HTTP_METH_POST);

$request->setBody('{"days_of_week":{},"email_address":"<ADD STRING VALUE>","end_hour":{},"expires_after":{},"list_order":{},"list_type":{},"minute_frequency":{},"send_type":{},"start_hour":{},"time_zone":{}}');

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}