<?php

$client = new http\Client;
$request = new http\Client\Request;

$body = new http\Message\Body;
$body->append('{"alert_id":0,"count":false,"sort_parameter":"<ADD STRING VALUE>","item_count":0,"page_number":0,"origin_city":"<ADD STRING VALUE>","origin_radius":0,"origin_state":["<ADD STRING VALUE>"],"destination_city":"<ADD STRING VALUE>","destination_radius":0,"destination_state":["<ADD STRING VALUE>"],"load_size":"Full","only_new":false,"ship_date":["<ADD STRING VALUE>"],"trailer_type":["<ADD STRING VALUE>"]}');

$request->setRequestUrl('https://www.directfreight.com/api/boards/%7Blist_type%7D');
$request->setRequestMethod('POST');
$request->setBody($body);

$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();