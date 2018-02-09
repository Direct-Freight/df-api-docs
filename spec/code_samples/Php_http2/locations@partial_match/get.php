<?php

$client = new http\Client;
$request = new http\Client\Request;

$request->setRequestUrl('https://www.directfreight.com/api/locations/partial_match');
$request->setRequestMethod('GET');
$request->setQuery(new http\QueryString(array(
  'term' => 'SOME_STRING_VALUE',
  'search_type' => 'SOME_STRING_VALUE'
)));

$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();