<?php

$client = new http\Client;
$request = new http\Client\Request;

$body = new http\Message\Body;
$body->append('{"alert_id":5555,"count":false,"destination_city":"chicago","destination_radius":0,"destination_state":["<ADD STRING VALUE>"],"item_count":0,"load_size":"Full","only_new":false,"origin_city":"chillicothe","origin_radius":0,"origin_state":["<ADD STRING VALUE>"],"page_number":0,"ship_date":["<ADD STRING VALUE>"],"total_items":0,"total_pages":0,"trailer_type":["<ADD STRING VALUE>"]}');

$request->setRequestUrl('https://www.directfreight.com/api/boards/%7Bboard_type%7D');
$request->setRequestMethod('POST');
$request->setBody($body);

$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();