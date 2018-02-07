<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => "https://www.directfreight.com/api/boards/%7Bboard_type%7D",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => "{\"alert_id\":5555,\"count\":false,\"destination_city\":\"chicago\",\"destination_radius\":0,\"destination_state\":[\"<ADD STRING VALUE>\"],\"item_count\":0,\"load_size\":\"Full\",\"only_new\":false,\"origin_city\":\"chillicothe\",\"origin_radius\":0,\"origin_state\":[\"<ADD STRING VALUE>\"],\"page_number\":0,\"ship_date\":[\"<ADD STRING VALUE>\"],\"total_items\":0,\"total_pages\":0,\"trailer_type\":[\"<ADD STRING VALUE>\"]}",
));

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}