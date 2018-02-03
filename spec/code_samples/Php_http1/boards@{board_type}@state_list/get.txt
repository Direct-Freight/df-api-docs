<?php

$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/boards/%7Bboard_type%7D/state_list');
$request->setMethod(HTTP_METH_GET);

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