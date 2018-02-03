<?php

$client = new http\Client;
$request = new http\Client\Request;

$request->setRequestUrl('https://www.directfreight.com/api/boards/%7Bboard_type%7D');
$request->setRequestMethod('PARAMETERS');
$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();