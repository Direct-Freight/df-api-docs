<?php

$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/billings');
$request->setMethod(HTTP_METH_POST);

$request->setBody('{"billing_address":{},"cc_data":{},"check_data":{},"promo_code":"<ADD STRING VALUE>"}');

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}