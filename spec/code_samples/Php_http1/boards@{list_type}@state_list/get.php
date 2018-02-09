<?php

$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/boards/%7Blist_type%7D/state_list');
$request->setMethod(HTTP_METH_GET);

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}