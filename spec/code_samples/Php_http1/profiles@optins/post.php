<?php

$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/profiles/optins');
$request->setMethod(HTTP_METH_POST);

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}