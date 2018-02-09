<?php

$client = new http\Client;
$request = new http\Client\Request;

$request->setRequestUrl('https://www.directfreight.com/api/locations/closest_city');
$request->setRequestMethod('GET');
$request->setQuery(new http\QueryString(array(
  'latitude' => 'SOME_NUMBER_VALUE',
  'longitude' => 'SOME_NUMBER_VALUE'
)));

$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();