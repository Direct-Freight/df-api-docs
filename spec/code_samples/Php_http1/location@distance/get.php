<?php

$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/location/distance');
$request->setMethod(HTTP_METH_GET);

$request->setQueryData(array(
  'origin_city' => 'SOME_STRING_VALUE',
  'origin_state' => 'SOME_STRING_VALUE',
  'destination_city' => 'SOME_STRING_VALUE',
  'destination_state' => 'SOME_STRING_VALUE'
));

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}