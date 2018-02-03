<?php

$client = new http\Client;
$request = new http\Client\Request;

$request->setRequestUrl('https://www.directfreight.com/api/alerts/%7Balert_type%7D');
$request->setRequestMethod('GET');
$request->setQuery(new http\QueryString(array(
  'alert_id' => 'SOME_ARRAY_VALUE'
)));

$request->setHeaders(array(
  'end-user-token' => 'SOME_STRING_VALUE',
  'content-type' => 'application/json',
  'accept' => 'application/json'
));

$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();