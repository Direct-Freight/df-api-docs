<?php

HttpRequest::methodRegister('PARAMETERS');
$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/boards/%7Bboard_type%7D');
$request->setMethod(HttpRequest::HTTP_METH_PARAMETERS);

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}