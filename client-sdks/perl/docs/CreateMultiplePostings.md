# WWW::SwaggerClient::Object::CreateMultiplePostings

## Load the model package
```perl
use WWW::SwaggerClient::Object::CreateMultiplePostings;
```

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_fax** | **string** | By default we use the number listed in their profile.  | [optional] 
**contact_name** | **string** | The dispatchers name. By default we use the profile information.  | [optional] 
**contact_phone** | **string** | By default we use the number listed in their profile.  | [optional] 
**delete_current_before_posting** | **boolean** | An optional argument that will first delete all of the users loads before entering the fresh list. Caution, this will still delete everything even if some of the entries fail to be created.  | [optional] 
**list** | **ARRAY[string]** | Valid types are &amp;quot;loads&amp;quot;, &amp;quot;trucks&amp;quot;, &amp;quot;private_loads&amp;quot;, &amp;quot;private_trucks&amp;quot;, &amp;quot;test_loads&amp;quot;, and &amp;quot;test_trucks&amp;quot;  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


