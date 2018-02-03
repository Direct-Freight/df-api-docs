<?php

$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/postings/multiple/%7Bposting_type%7D');
$request->setMethod(HTTP_METH_POST);

$request->setHeaders(array(
  'end-user-token' => 'SOME_STRING_VALUE',
  'content-type' => 'application/json',
  'accept' => 'application/json'
));

$request->setBody('{"contact_fax":"<ADD STRING VALUE>","contact_name":"<ADD STRING VALUE>","contact_phone":"<ADD STRING VALUE>","delete_current_before_posting":false,"list":["<ADD STRING VALUE>"]}');

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}