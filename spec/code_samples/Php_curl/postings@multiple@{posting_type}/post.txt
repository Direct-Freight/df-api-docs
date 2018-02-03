<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => "https://www.directfreight.com/api/postings/multiple/%7Bposting_type%7D",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => "{\"contact_fax\":\"<ADD STRING VALUE>\",\"contact_name\":\"<ADD STRING VALUE>\",\"contact_phone\":\"<ADD STRING VALUE>\",\"delete_current_before_posting\":false,\"list\":[\"<ADD STRING VALUE>\"]}",
  CURLOPT_HTTPHEADER => array(
    "accept: application/json",
    "content-type: application/json",
    "end-user-token: SOME_STRING_VALUE"
  ),
));

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}