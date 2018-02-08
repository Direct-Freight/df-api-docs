<?php

$client = new http\Client;
$request = new http\Client\Request;

$request->setRequestUrl('https://www.directfreight.com/api/postings/%7Bposting_type%7D');
$request->setRequestMethod('DELETE');
$request->setQuery(new http\QueryString(array(
  'posting_id' => 'SOME_ARRAY_VALUE'
)));

$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();