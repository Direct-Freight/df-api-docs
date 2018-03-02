<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => "https://www.directfreight.com/api/boards/%7Blist_type%7D",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => "{\"alert_id\":0,\"count\":false,\"sort_parameter\":\"<ADD STRING VALUE>\",\"item_count\":0,\"page_number\":0,\"origin_city\":\"<ADD STRING VALUE>\",\"origin_radius\":0,\"origin_state\":[\"<ADD STRING VALUE>\"],\"destination_city\":\"<ADD STRING VALUE>\",\"destination_radius\":0,\"destination_state\":[\"<ADD STRING VALUE>\"],\"load_size\":\"Full\",\"only_new\":false,\"ship_date\":[\"<ADD STRING VALUE>\"],\"trailer_type\":[\"<ADD STRING VALUE>\"]}",
));

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}