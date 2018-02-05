<?php

$client = new http\Client;
$request = new http\Client\Request;

$body = new http\Message\Body;
$body->append('{"email":"<ADD STRING VALUE>","end-user-token":"<ADD STRING VALUE>","password":"<ADD STRING VALUE>"}');

$request->setRequestUrl('https://www.directfreight.com/api/end_user_authentication/users');
$request->setRequestMethod('POST');
$request->setBody($body);

$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();