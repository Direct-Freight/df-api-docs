<?php

$client = new http\Client;
$request = new http\Client\Request;

$body = new http\Message\Body;
$body->append('{"The":{}}');

$request->setRequestUrl('https://www.directfreight.com/api/profiles/documents');
$request->setRequestMethod('POST');
$request->setBody($body);

$request->setHeaders(array(
  'end-user-token' => 'SOME_STRING_VALUE'
));

$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();