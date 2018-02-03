<?php

$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/end_user_authentications/passwords');
$request->setMethod(HTTP_METH_GET);

$request->setQueryData(array(
  'email' => 'SOME_STRING_VALUE'
));

$request->setHeaders(array(
  'content-type' => 'application/json',
  'accept' => 'application/json'
));

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}