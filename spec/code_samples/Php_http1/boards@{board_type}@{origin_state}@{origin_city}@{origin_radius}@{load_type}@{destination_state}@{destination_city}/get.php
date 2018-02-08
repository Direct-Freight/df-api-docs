<?php

$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/boards/%7Bboard_type%7D/%7Borigin_state%7D/%7Borigin_city%7D/%7Borigin_radius%7D/%7Bload_type%7D/%7Bdestination_state%7D/%7Bdestination_city%7D');
$request->setMethod(HTTP_METH_GET);

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}