<?php

$client = new http\Client;
$request = new http\Client\Request;

$request->setRequestUrl('https://www.directfreight.com/api/boards/%7Bboard_type%7D/%7Borigin_state%7D/%7Borigin_city%7D/%7Borigin_radius%7D/%7Bload_type%7D/%7Bdestination_state%7D/%7Bdestination_city%7D');
$request->setRequestMethod('GET');
$request->setHeaders(array(
  'end-user-token' => 'SOME_STRING_VALUE',
  'content-type' => 'application/json',
  'accept' => 'application/json'
));

$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();