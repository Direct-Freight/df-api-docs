<?php

HttpRequest::methodRegister('PATCH');
$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/boards/hidden_entries');
$request->setMethod(HttpRequest::HTTP_METH_PATCH);

$request->setBody('{"entry_id":["<ADD STRING VALUE>"]}');

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}