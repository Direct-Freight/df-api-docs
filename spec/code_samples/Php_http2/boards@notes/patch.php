<?php

$client = new http\Client;
$request = new http\Client\Request;

$body = new http\Message\Body;
$body->append('{"body":"<ADD STRING VALUE>","title":"<ADD STRING VALUE>"}');

$request->setRequestUrl('https://www.directfreight.com/api/boards/notes');
$request->setRequestMethod('PATCH');
$request->setBody($body);

$request->setHeaders(array(
  'end-user-token' => 'SOME_STRING_VALUE',
  'content-type' => 'application/json',
  'accept' => 'application/json'
));

$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();