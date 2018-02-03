<?php

$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/boards/notes');
$request->setMethod(HTTP_METH_DELETE);

$request->setQueryData(array(
  'note_id' => 'SOME_STRING_VALUE'
));

$request->setHeaders(array(
  'end-user-token' => 'SOME_STRING_VALUE',
  'content-type' => 'application/json',
  'accept' => 'application/json'
));

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}