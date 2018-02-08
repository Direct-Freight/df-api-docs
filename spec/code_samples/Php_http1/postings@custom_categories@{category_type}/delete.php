<?php

$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/postings/custom_categories/%7Bcategory_type%7D');
$request->setMethod(HTTP_METH_DELETE);

$request->setQueryData(array(
  'category_id' => 'SOME_ARRAY_VALUE'
));

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}