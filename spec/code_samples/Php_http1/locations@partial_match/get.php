<?php

$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/locations/partial_match');
$request->setMethod(HTTP_METH_GET);

$request->setQueryData(array(
  'term' => 'SOME_STRING_VALUE',
  'search_type' => 'SOME_STRING_VALUE'
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