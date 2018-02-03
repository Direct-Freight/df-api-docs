<?php

HttpRequest::methodRegister('PATCH');
$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/boards/hidden_entries');
$request->setMethod(HttpRequest::HTTP_METH_PATCH);

$request->setHeaders(array(
  'end-user-token' => 'SOME_STRING_VALUE',
  'content-type' => 'application/json',
  'accept' => 'application/json'
));

$request->setBody('{"entry_id":["<ADD STRING VALUE>"]}');

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}