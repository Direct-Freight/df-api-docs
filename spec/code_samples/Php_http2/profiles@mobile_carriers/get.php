<?php

$client = new http\Client;
$request = new http\Client\Request;

$body = new http\Message\Body;
$body->append('{"carrier_id":0}');

$request->setRequestUrl('https://www.directfreight.com/api/profiles/mobile_carriers');
$request->setRequestMethod('GET');
$request->setBody($body);

$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();