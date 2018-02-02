# WWW::SwaggerClient::Object::PatchAlertProperties

## Load the model package
```perl
use WWW::SwaggerClient::Object::PatchAlertProperties;
```

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days_of_week** | **object** | Limit the days that alerts are sent to the days listed. Send an array of strings. Valid strings are &#39;Sun&#39;,&#39;Mon&#39;,&#39;Tue&#39;,&#39;Wed&#39;,&#39;Thu&#39;,&#39;Fri&#39;,and &#39;Sat&#39;. | [optional] 
**end_hour** | **object** | Has the same values as start_hour | [optional] 
**expires_after** | **object** | The last day the alert will be valid. Valid time frames are from today until one year into the future. | [optional] 
**list_order** | **object** | Any value that is valid in the boards sort_order is also valid here. | [optional] 
**list_type** | **object** | This specify the type of list that is returned, including disabling the list from being sent at all. Valid values are &#39;complete-list&#39;,&#39;only-new&#39;, and &#39;not-active&#39;. | [optional] 
**minute_frequency** | **object** | How many minutes to wait before sending another alert. Valid values are &#39;15&#39;,&#39;30&#39;,&#39;60&#39;,&#39;120&#39;,&#39;240&#39;,&#39;480&#39;, and &#39;1440&#39;. | [optional] 
**send_type** | **object** | What method to send the alert list. Valid types are &#39;email&#39;,or &#39;text&#39;. | [optional] 
**start_hour** | **object** | A value between 3-21 corresponding to the hour of the day. | [optional] 
**time_zone** | **object** | A number between -1 and 2. -1 &#x3D; EST, 0 &#x3D; CST, 1 &#x3D; MST, 2 &#x3D; PST | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


