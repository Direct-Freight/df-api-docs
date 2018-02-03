<?php

$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/boards/hidden_companies');
$request->setMethod(HTTP_METH_POST);

$request->setHeaders(array(
  'end-user-token' => 'SOME_STRING_VALUE',
  'content-type' => 'application/json',
  'accept' => 'application/json'
));

$request->setBody('{"company_name":"<ADD STRING VALUE>"}');

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}