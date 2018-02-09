<?php

$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/locations/closest_city');
$request->setMethod(HTTP_METH_GET);

$request->setQueryData(array(
  'latitude' => 'SOME_NUMBER_VALUE',
  'longitude' => 'SOME_NUMBER_VALUE'
));

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}