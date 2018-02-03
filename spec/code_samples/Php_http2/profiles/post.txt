<?php

$client = new http\Client;
$request = new http\Client\Request;

$body = new http\Message\Body;
$body->append('{"address":"<ADD STRING VALUE>","city":"<ADD STRING VALUE>","company":"<ADD STRING VALUE>","contact_extension":"<ADD STRING VALUE>","contact_name":"<ADD STRING VALUE>","contact_number":"<ADD STRING VALUE>","dot_number":"<ADD STRING VALUE>","fax_number":"<ADD STRING VALUE>","mc_number":"<ADD STRING VALUE>","mobile_carrier":0,"mobile_number":"<ADD STRING VALUE>","password":"<ADD STRING VALUE>","state":"<ADD STRING VALUE>","web_page":"<ADD STRING VALUE>","zip":"<ADD STRING VALUE>"}');

$request->setRequestUrl('https://www.directfreight.com/api/profiles');
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