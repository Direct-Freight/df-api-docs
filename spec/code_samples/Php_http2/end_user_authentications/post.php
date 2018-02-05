<?php

$client = new http\Client;
$request = new http\Client\Request;

$body = new http\Message\Body;
$body->append('{"login":"<ADD STRING VALUE>","realm":"<ADD STRING VALUE>","secret":"<ADD STRING VALUE>"}');

$request->setRequestUrl('https://www.directfreight.com/api/end_user_authentications');
$request->setRequestMethod('POST');
$request->setBody($body);

$request->setQuery(new http\QueryString(array(
  '' => 'SOME_STRING_VALUE'
)));

$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();