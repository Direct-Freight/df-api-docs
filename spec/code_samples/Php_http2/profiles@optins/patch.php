<?php

$client = new http\Client;
$request = new http\Client\Request;

$request->setRequestUrl('https://www.directfreight.com/api/profiles/optins');
$request->setRequestMethod('PATCH');
$request->setHeaders(array(
  'end-user-token' => 'SOME_STRING_VALUE'
));

$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();