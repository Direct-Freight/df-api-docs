<?php

$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/credit_reports');
$request->setMethod(HTTP_METH_GET);

$request->setQueryData(array(
  'credit_report_id' => 'SOME_STRING_VALUE',
  'format' => 'SOME_STRING_VALUE'
));

$request->setHeaders(array(
  'end-user-token' => 'SOME_STRING_VALUE'
));

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}