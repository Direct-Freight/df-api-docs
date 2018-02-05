<?php

$client = new http\Client;
$request = new http\Client\Request;

$body = new http\Message\Body;
$body->append('{"body":"<ADD STRING VALUE>","entry_id":0,"title":"<ADD STRING VALUE>"}');

$request->setRequestUrl('https://www.directfreight.com/api/boards/notes');
$request->setRequestMethod('POST');
$request->setBody($body);

$request->setHeaders(array(
  'end-user-token' => 'SOME_STRING_VALUE'
));

$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();