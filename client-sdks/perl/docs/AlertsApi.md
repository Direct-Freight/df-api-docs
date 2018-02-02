# WWW::SwaggerClient::AlertsApi

## Load the API package
```perl
use WWW::SwaggerClient::Object::AlertsApi;
```

All URIs are relative to *https://www.directfreight.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alerts_alert_type_delete**](AlertsApi.md#alerts_alert_type_delete) | **DELETE** /alerts/{alert_type} | Delete an alert.
[**alerts_alert_type_get**](AlertsApi.md#alerts_alert_type_get) | **GET** /alerts/{alert_type} | Get a list of alerts.
[**alerts_alert_type_patch**](AlertsApi.md#alerts_alert_type_patch) | **PATCH** /alerts/{alert_type} | Update an alert.
[**alerts_alert_type_post**](AlertsApi.md#alerts_alert_type_post) | **POST** /alerts/{alert_type} | Create an alert.


# **alerts_alert_type_delete**
> alerts_alert_type_delete(alert_type => $alert_type, end_user_token => $end_user_token, alert_id => $alert_id)

Delete an alert.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::AlertsApi->new();
my $alert_type = 'alert_type_example'; # string | Valid types are \"loads\", and \"trucks\".
my $end_user_token = 'end_user_token_example'; # string | 
my $alert_id = (); # ARRAY[string] | Specify to just delete some alerts.

eval { 
    $api_instance->alerts_alert_type_delete(alert_type => $alert_type, end_user_token => $end_user_token, alert_id => $alert_id);
};
if ($@) {
    warn "Exception when calling AlertsApi->alerts_alert_type_delete: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_type** | **string**| Valid types are \&quot;loads\&quot;, and \&quot;trucks\&quot;. | 
 **end_user_token** | **string**|  | 
 **alert_id** | [**ARRAY[string]**](string.md)| Specify to just delete some alerts. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alerts_alert_type_get**
> GetAlertResponse alerts_alert_type_get(alert_type => $alert_type, end_user_token => $end_user_token, alert_id => $alert_id)

Get a list of alerts.

Get a list of alerts.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::AlertsApi->new();
my $alert_type = 'alert_type_example'; # string | Valid types are \"loads\", and \"trucks\".
my $end_user_token = 'end_user_token_example'; # string | 
my $alert_id = (); # ARRAY[UUID] | only get a subset of alerts. As this is a get request this is specified as a query string parameter.

eval { 
    my $result = $api_instance->alerts_alert_type_get(alert_type => $alert_type, end_user_token => $end_user_token, alert_id => $alert_id);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling AlertsApi->alerts_alert_type_get: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_type** | **string**| Valid types are \&quot;loads\&quot;, and \&quot;trucks\&quot;. | 
 **end_user_token** | **string**|  | 
 **alert_id** | [**ARRAY[UUID]**](UUID.md)| only get a subset of alerts. As this is a get request this is specified as a query string parameter. | [optional] 

### Return type

[**GetAlertResponse**](GetAlertResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alerts_alert_type_patch**
> PatchAlertResponse alerts_alert_type_patch(alert_type => $alert_type, end_user_token => $end_user_token, alert_id => $alert_id, body => $body)

Update an alert.

Search objects are set at creation. You cannot modify them after the alert has been created.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::AlertsApi->new();
my $alert_type = 'alert_type_example'; # string | Valid types are \"loads\", and \"trucks\".
my $end_user_token = 'end_user_token_example'; # string | 
my $alert_id = 'alert_id_example'; # string | Specify which alert you are updating.
my $body = WWW::SwaggerClient::Object::PatchAlertProperties->new(); # PatchAlertProperties | 

eval { 
    my $result = $api_instance->alerts_alert_type_patch(alert_type => $alert_type, end_user_token => $end_user_token, alert_id => $alert_id, body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling AlertsApi->alerts_alert_type_patch: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_type** | **string**| Valid types are \&quot;loads\&quot;, and \&quot;trucks\&quot;. | 
 **end_user_token** | **string**|  | 
 **alert_id** | **string**| Specify which alert you are updating. | 
 **body** | [**PatchAlertProperties**](PatchAlertProperties.md)|  | [optional] 

### Return type

[**PatchAlertResponse**](PatchAlertResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alerts_alert_type_post**
> PostAlertResponse alerts_alert_type_post(alert_type => $alert_type, end_user_token => $end_user_token, body => $body)

Create an alert.

Any parameter that is defined here and is also defined on the boards GET, follows the same rules.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::AlertsApi->new();
my $alert_type = 'alert_type_example'; # string | Valid types are \"loads\", and \"trucks\".
my $end_user_token = 'end_user_token_example'; # string | 
my $body = WWW::SwaggerClient::Object::AlertProperties->new(); # AlertProperties | 

eval { 
    my $result = $api_instance->alerts_alert_type_post(alert_type => $alert_type, end_user_token => $end_user_token, body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling AlertsApi->alerts_alert_type_post: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_type** | **string**| Valid types are \&quot;loads\&quot;, and \&quot;trucks\&quot;. | 
 **end_user_token** | **string**|  | 
 **body** | [**AlertProperties**](AlertProperties.md)|  | 

### Return type

[**PostAlertResponse**](PostAlertResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

