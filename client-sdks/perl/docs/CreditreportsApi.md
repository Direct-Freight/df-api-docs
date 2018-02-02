# WWW::SwaggerClient::CreditreportsApi

## Load the API package
```perl
use WWW::SwaggerClient::Object::CreditreportsApi;
```

All URIs are relative to *https://www.directfreight.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**credit_reports_get**](CreditreportsApi.md#credit_reports_get) | **GET** /credit_reports | Request access to a credit report.


# **credit_reports_get**
> credit_reports_get(end_user_token => $end_user_token, credit_report_id => $credit_report_id, format => $format)

Request access to a credit report.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::CreditreportsApi->new();
my $end_user_token = 'end_user_token_example'; # string | The logged in user's token.
my $credit_report_id = 'credit_report_id_example'; # string | A special id returned with the board entries.
my $format = 'format_example'; # string | Return format. Currently only supports html and json.

eval { 
    $api_instance->credit_reports_get(end_user_token => $end_user_token, credit_report_id => $credit_report_id, format => $format);
};
if ($@) {
    warn "Exception when calling CreditreportsApi->credit_reports_get: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_user_token** | **string**| The logged in user&#39;s token. | 
 **credit_report_id** | **string**| A special id returned with the board entries. | 
 **format** | **string**| Return format. Currently only supports html and json. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

