<?php

$client = new http\Client;
$request = new http\Client\Request;

$request->setRequestUrl('https://www.directfreight.com/api/locations/partial_match');
$request->setRequestMethod('GET');
$request->setQuery(new http\QueryString(array(
  'term' => 'SOME_STRING_VALUE',
  'search_type' => 'SOME_STRING_VALUE'
)));

$request->setHeaders(array(
  'content-type' => 'application/json',
  'accept' => 'application/json'
));

$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();