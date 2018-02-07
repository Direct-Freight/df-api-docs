<?php

$request = new HttpRequest();
$request->setUrl('https://www.directfreight.com/api/profiles');
$request->setMethod(HTTP_METH_POST);

$request->setHeaders(array(
  'end-user-token' => 'SOME_STRING_VALUE'
));

$request->setBody('{"address":"<ADD STRING VALUE>","city":"<ADD STRING VALUE>","company":"<ADD STRING VALUE>","contact_extension":"<ADD STRING VALUE>","contact_name":"<ADD STRING VALUE>","contact_number":"<ADD STRING VALUE>","dot_number":"<ADD STRING VALUE>","fax_number":"<ADD STRING VALUE>","mc_number":"<ADD STRING VALUE>","mobile_carrier":0,"mobile_number":"<ADD STRING VALUE>","password":"<ADD STRING VALUE>","state":"<ADD STRING VALUE>","web_page":"<ADD STRING VALUE>","zip":"<ADD STRING VALUE>"}');

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}