<?php

$client = new http\Client;
$request = new http\Client\Request;

$body = new http\Message\Body;
$body->append('{"days_of_week":{},"end_hour":{},"expires_after":{},"list_order":{},"list_type":{},"minute_frequency":{},"send_type":{},"start_hour":{},"time_zone":{}}');

$request->setRequestUrl('https://www.directfreight.com/api/alerts/%7Blist_type%7D');
$request->setRequestMethod('PATCH');
$request->setBody($body);

$request->setQuery(new http\QueryString(array(
  'alert_id' => 'SOME_STRING_VALUE'
)));

$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();