<?php

$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/postings/%7Blist_type%7D');
$request->setMethod(HTTP_METH_GET);

$request->setQueryData(array(
  'posting_id' => 'SOME_ARRAY_VALUE'
));

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}