<?php

$client = new http\Client;
$request = new http\Client\Request;

$request->setRequestUrl('https://www.directfreight.com/api/end_user_authentications/passwords');
$request->setRequestMethod('GET');
$request->setQuery(new http\QueryString(array(
  'email' => 'SOME_STRING_VALUE'
)));

$request->setHeaders(array(
  'content-type' => 'application/json',
  'accept' => 'application/json'
));

$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();