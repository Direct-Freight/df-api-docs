<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => "https://www.directfreight.com/api/profiles",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "PATCH",
  CURLOPT_POSTFIELDS => "{\"address\":\"<ADD STRING VALUE>\",\"city\":\"<ADD STRING VALUE>\",\"company\":\"<ADD STRING VALUE>\",\"contact_extension\":\"<ADD STRING VALUE>\",\"contact_name\":\"<ADD STRING VALUE>\",\"contact_number\":\"<ADD STRING VALUE>\",\"dot_number\":\"<ADD STRING VALUE>\",\"fax_number\":\"<ADD STRING VALUE>\",\"mc_number\":\"<ADD STRING VALUE>\",\"mobile_carrier\":0,\"mobile_number\":\"<ADD STRING VALUE>\",\"state\":\"<ADD STRING VALUE>\",\"web_page\":\"<ADD STRING VALUE>\",\"zip\":\"<ADD STRING VALUE>\"}",
  CURLOPT_HTTPHEADER => array(
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