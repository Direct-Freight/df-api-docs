<?php

$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/boards/%7Bboard_type%7D');
$request->setMethod(HTTP_METH_POST);

$request->setHeaders(array(
  'content-type' => 'application/json',
  'accept' => 'application/json'
));

$request->setBody('{"alert_id":false,"count":false,"destination_city":"<ADD STRING VALUE>","destination_radius":0,"destination_state":["<ADD STRING VALUE>"],"item_count":0,"load_size":["<ADD STRING VALUE>"],"only_new":false,"origin_city":"<ADD STRING VALUE>","origin_radius":0,"origin_state":["<ADD STRING VALUE>"],"page_number":0,"ship_date":["<ADD STRING VALUE>"],"total_items":0,"total_pages":0,"trailer_type":["<ADD STRING VALUE>"]}');

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}