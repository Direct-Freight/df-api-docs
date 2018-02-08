<?php

$client = new http\Client;
$request = new http\Client\Request;

$request->setRequestUrl('https://www.directfreight.com/api/end_user_authentications');
$request->setRequestMethod('DELETE');
$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();