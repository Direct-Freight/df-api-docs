<?php

$client = new http\Client;
$request = new http\Client\Request;

$request->setRequestUrl('https://www.directfreight.com/api/location/distance');
$request->setRequestMethod('GET');
$request->setQuery(new http\QueryString(array(
  'origin_city' => 'SOME_STRING_VALUE',
  'origin_state' => 'SOME_STRING_VALUE',
  'destination_city' => 'SOME_STRING_VALUE',
  'destination_state' => 'SOME_STRING_VALUE'
)));

$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();