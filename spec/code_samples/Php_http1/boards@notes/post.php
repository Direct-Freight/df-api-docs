<?php

$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/boards/notes');
$request->setMethod(HTTP_METH_POST);

$request->setHeaders(array(
  'end-user-token' => 'SOME_STRING_VALUE'
));

$request->setBody('{"body":"<ADD STRING VALUE>","entry_id":0,"title":"<ADD STRING VALUE>"}');

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}