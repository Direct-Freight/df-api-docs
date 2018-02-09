<?php

HttpRequest::methodRegister('PATCH');
$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/boards/notes');
$request->setMethod(HttpRequest::HTTP_METH_PATCH);

$request->setBody('{"body":"<ADD STRING VALUE>","title":"<ADD STRING VALUE>"}');

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}