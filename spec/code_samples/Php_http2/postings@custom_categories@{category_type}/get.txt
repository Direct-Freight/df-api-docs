<?php

$client = new http\Client;
$request = new http\Client\Request;

$request->setRequestUrl('https://www.directfreight.com/api/postings/custom_categories/%7Bcategory_type%7D');
$request->setRequestMethod('GET');
$request->setQuery(new http\QueryString(array(
  'category_id' => 'SOME_ARRAY_VALUE'
)));

$request->setHeaders(array(
  'end-user-token' => 'SOME_STRING_VALUE',
  'content-type' => 'application/json',
  'accept' => 'application/json'
));

$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();