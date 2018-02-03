<?php

$client = new http\Client;
$request = new http\Client\Request;

$body = new http\Message\Body;
$body->append('{"days_of_week":{},"email_address":"<ADD STRING VALUE>","end_hour":{},"expires_after":{},"list_order":{},"list_type":{},"minute_frequency":{},"send_type":{},"start_hour":{},"time_zone":{}}');

$request->setRequestUrl('https://www.directfreight.com/api/alerts/%7Balert_type%7D');
$request->setRequestMethod('POST');
$request->setBody($body);

$request->setHeaders(array(
  'end-user-token' => 'SOME_STRING_VALUE',
  'content-type' => 'application/json',
  'accept' => 'application/json'
));

$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();