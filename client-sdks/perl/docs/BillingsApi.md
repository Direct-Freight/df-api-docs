# WWW::SwaggerClient::BillingsApi

## Load the API package
```perl
use WWW::SwaggerClient::Object::BillingsApi;
```

All URIs are relative to *https://www.directfreight.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billings_get**](BillingsApi.md#billings_get) | **GET** /billings | Returns the amount the end user will be charged. If a promo code is present return adjusted amount. If there are special conditions a string with the promo code benefits will also be returned.
[**billings_post**](BillingsApi.md#billings_post) | **POST** /billings | This function will attempt to process a payment, and upgrade a non subscibed user. 


# **billings_get**
> GetBillingResponse billings_get(end_user_token => $end_user_token, promo_code => $promo_code)

Returns the amount the end user will be charged. If a promo code is present return adjusted amount. If there are special conditions a string with the promo code benefits will also be returned.

Will return how much the end user will be charged to upgrade. It will not charge the user, or consume the promo code.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::BillingsApi->new();
my $end_user_token = 'end_user_token_example'; # string | 
my $promo_code = 'promo_code_example'; # string | The promo code. 

eval { 
    my $result = $api_instance->billings_get(end_user_token => $end_user_token, promo_code => $promo_code);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling BillingsApi->billings_get: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_user_token** | **string**|  | 
 **promo_code** | **string**| The promo code.  | [optional] 

### Return type

[**GetBillingResponse**](GetBillingResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billings_post**
> PostBillingResponse billings_post(end_user_token => $end_user_token, body => $body)

This function will attempt to process a payment, and upgrade a non subscibed user. 

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::BillingsApi->new();
my $end_user_token = 'end_user_token_example'; # string | 
my $body = WWW::SwaggerClient::Object::BillUser->new(); # BillUser | This function will attempt to process a payment, and upgrade a non subscibed user. 

eval { 
    my $result = $api_instance->billings_post(end_user_token => $end_user_token, body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling BillingsApi->billings_post: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_user_token** | **string**|  | 
 **body** | [**BillUser**](BillUser.md)| This function will attempt to process a payment, and upgrade a non subscibed user.  | 

### Return type

[**PostBillingResponse**](PostBillingResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

