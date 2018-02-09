<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => "https://www.directfreight.com/api/postings/%7Blist_type%7D",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "PATCH",
  CURLOPT_POSTFIELDS => "{\"comment\":{},\"custom_id\":{},\"destination_city\":{},\"destination_state\":{},\"height\":{},\"length\":{},\"load_size\":{},\"origin_city\":{},\"origin_state\":{},\"other_trailer_types\":{},\"pay_rate\":{},\"posting_id\":0,\"receive_date\":{},\"ship_date\":{},\"trailer_type\":{},\"weight\":{},\"width\":{}}",
));

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}