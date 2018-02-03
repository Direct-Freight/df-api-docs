<?php

$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/end_user_authentications');
$request->setMethod(HTTP_METH_POST);

$request->setQueryData(array(
  '' => 'SOME_STRING_VALUE'
));

$request->setHeaders(array(
  'content-type' => 'application/json',
  'accept' => 'application/json'
));

$request->setBody('{"login":"<ADD STRING VALUE>","realm":"<ADD STRING VALUE>","secret":"<ADD STRING VALUE>"}');

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}