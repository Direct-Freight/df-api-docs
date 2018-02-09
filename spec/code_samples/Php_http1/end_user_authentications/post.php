<?php

$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/end_user_authentications');
$request->setMethod(HTTP_METH_POST);

$request->setBody('{"login":"<ADD STRING VALUE>","realm":"username","secret":"<ADD STRING VALUE>"}');

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}