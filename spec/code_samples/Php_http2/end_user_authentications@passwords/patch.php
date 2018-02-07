<?php

$client = new http\Client;
$request = new http\Client\Request;

$body = new http\Message\Body;
$body->append('{"new_password":"<ADD STRING VALUE>","old_password":"<ADD STRING VALUE>"}');

$request->setRequestUrl('https://www.directfreight.com/api/end_user_authentications/passwords');
$request->setRequestMethod('PATCH');
$request->setBody($body);

$request->setHeaders(array(
  'end-user-token' => 'SOME_STRING_VALUE'
));

$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();