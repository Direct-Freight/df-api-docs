<?php

$client = new http\Client;
$request = new http\Client\Request;

$body = new http\Message\Body;
$body->append('{"company_id":"<ADD STRING VALUE>"}');

$request->setRequestUrl('https://www.directfreight.com/api/boards/hidden_companies');
$request->setRequestMethod('PATCH');
$request->setBody($body);

$request->setHeaders(array(
  'end-user-token' => 'SOME_STRING_VALUE'
));

$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();