# WWW::SwaggerClient::ValidationsApi

## Load the API package
```perl
use WWW::SwaggerClient::Object::ValidationsApi;
```

All URIs are relative to *https://www.directfreight.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validations_email_exists_get**](ValidationsApi.md#validations_email_exists_get) | **GET** /validations/email_exists | Check if an e-mail exists.


# **validations_email_exists_get**
> GetEmailExistsResponse validations_email_exists_get(end_user_token => $end_user_token, email => $email)

Check if an e-mail exists.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::ValidationsApi->new();
my $end_user_token = 'end_user_token_example'; # string | The logged in user's token.
my $email = 'email_example'; # string | Enter an e-mail to see if it is available. Can be used as ?email=xxx or as a JSON request.

eval { 
    my $result = $api_instance->validations_email_exists_get(end_user_token => $end_user_token, email => $email);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling ValidationsApi->validations_email_exists_get: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_user_token** | **string**| The logged in user&#39;s token. | 
 **email** | **string**| Enter an e-mail to see if it is available. Can be used as ?email&#x3D;xxx or as a JSON request. | 

### Return type

[**GetEmailExistsResponse**](GetEmailExistsResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

