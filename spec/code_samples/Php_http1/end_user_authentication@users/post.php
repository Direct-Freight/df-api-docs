<?php

$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/end_user_authentication/users');
$request->setMethod(HTTP_METH_POST);

$request->setBody('{"email":"<ADD STRING VALUE>","password":"<ADD STRING VALUE>"}');

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}