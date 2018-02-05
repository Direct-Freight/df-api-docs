<?php

$client = new http\Client;
$request = new http\Client\Request;

$request->setRequestUrl('https://www.directfreight.com/api/boards/notes');
$request->setRequestMethod('GET');
$request->setQuery(new http\QueryString(array(
  'entry_id' => 'SOME_ARRAY_VALUE'
)));

$request->setHeaders(array(
  'end-user-token' => 'SOME_STRING_VALUE'
));

$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();