<?php

HttpRequest::methodRegister('PATCH');
$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/end_user_authentications/passwords');
$request->setMethod(HttpRequest::HTTP_METH_PATCH);

$request->setHeaders(array(
  'end-user-token' => 'SOME_STRING_VALUE',
  'content-type' => 'application/json',
  'accept' => 'application/json'
));

$request->setBody('{"new_password":"<ADD STRING VALUE>","old_password":"<ADD STRING VALUE>"}');

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}