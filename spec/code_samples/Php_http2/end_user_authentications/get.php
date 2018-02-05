<?php

$client = new http\Client;
$request = new http\Client\Request;

$request->setRequestUrl('https://www.directfreight.com/api/end_user_authentications');
$request->setRequestMethod('GET');
$request->setQuery(new http\QueryString(array(
  '' => 'SOME_STRING_VALUE'
)));

$request->setHeaders(array(
  'end-user-token' => 'SOME_STRING_VALUE'
));

$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();