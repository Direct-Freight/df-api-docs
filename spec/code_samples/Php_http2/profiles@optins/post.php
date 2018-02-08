<?php

$client = new http\Client;
$request = new http\Client\Request;

$request->setRequestUrl('https://www.directfreight.com/api/profiles/optins');
$request->setRequestMethod('POST');
$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();