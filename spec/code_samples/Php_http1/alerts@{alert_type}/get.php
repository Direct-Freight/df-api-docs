<?php

$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/alerts/%7Balert_type%7D');
$request->setMethod(HTTP_METH_GET);

$request->setQueryData(array(
  'alert_id' => 'SOME_ARRAY_VALUE'
));

$request->setHeaders(array(
  'end-user-token' => 'SOME_STRING_VALUE',
  'content-type' => 'application/json',
  'accept' => 'application/json'
));

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}