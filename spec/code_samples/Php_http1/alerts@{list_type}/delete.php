<?php

$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/alerts/%7Blist_type%7D');
$request->setMethod(HTTP_METH_DELETE);

$request->setQueryData(array(
  'alert_id' => 'SOME_ARRAY_VALUE'
));

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}