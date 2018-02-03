<?php

$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/profiles/mobile_carriers');
$request->setMethod(HTTP_METH_GET);

$request->setHeaders(array(
  'content-type' => 'application/json',
  'accept' => 'application/json'
));

$request->setBody('{"carrier_id":0}');

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}