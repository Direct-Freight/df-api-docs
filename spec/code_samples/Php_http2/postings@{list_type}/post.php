<?php

$client = new http\Client;
$request = new http\Client\Request;

$body = new http\Message\Body;
$body->append('{"comment":{},"custom_id":{},"destination_city":{},"destination_state":{},"height":{},"length":{},"load_size":{},"origin_city":{},"origin_state":{},"other_trailer_types":{},"pay_rate":{},"posting_id":0,"receive_date":{},"ship_date":{},"trailer_type":{},"weight":{},"width":{}}');

$request->setRequestUrl('https://www.directfreight.com/api/postings/%7Blist_type%7D');
$request->setRequestMethod('POST');
$request->setBody($body);

$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();