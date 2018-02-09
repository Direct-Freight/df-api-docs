<?php

$client = new http\Client;
$request = new http\Client\Request;

$body = new http\Message\Body;
$body->append('{"login":"<ADD STRING VALUE>","realm":"username","secret":"<ADD STRING VALUE>"}');

$request->setRequestUrl('https://www.directfreight.com/api/end_user_authentications');
$request->setRequestMethod('POST');
$request->setBody($body);

$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();