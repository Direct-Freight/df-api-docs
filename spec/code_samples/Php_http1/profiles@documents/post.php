<?php

$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/profiles/documents');
$request->setMethod(HTTP_METH_POST);

$request->setHeaders(array(
  'end-user-token' => 'SOME_STRING_VALUE'
));

$request->setBody('{"The":{}}');

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}