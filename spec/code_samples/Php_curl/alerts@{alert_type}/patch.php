<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => "https://www.directfreight.com/api/alerts/%7Balert_type%7D?alert_id=SOME_STRING_VALUE",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "PATCH",
  CURLOPT_POSTFIELDS => "{\"days_of_week\":{},\"end_hour\":{},\"expires_after\":{},\"list_order\":{},\"list_type\":{},\"minute_frequency\":{},\"send_type\":{},\"start_hour\":{},\"time_zone\":{}}",
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