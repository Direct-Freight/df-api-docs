# WWW::SwaggerClient::EnduserauthenticationsApi

## Load the API package
```perl
use WWW::SwaggerClient::Object::EnduserauthenticationsApi;
```

All URIs are relative to *https://www.directfreight.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**end_user_authentication_users_post**](EnduserauthenticationsApi.md#end_user_authentication_users_post) | **POST** /end_user_authentication/users | Create a new user.
[**end_user_authentications_dates_get**](EnduserauthenticationsApi.md#end_user_authentications_dates_get) | **GET** /end_user_authentications/dates | Gets an authoritative date_time string.
[**end_user_authentications_delete**](EnduserauthenticationsApi.md#end_user_authentications_delete) | **DELETE** /end_user_authentications | Logs a user out.
[**end_user_authentications_get**](EnduserauthenticationsApi.md#end_user_authentications_get) | **GET** /end_user_authentications | Get current authentication level for the user.
[**end_user_authentications_passwords_get**](EnduserauthenticationsApi.md#end_user_authentications_passwords_get) | **GET** /end_user_authentications/passwords | Request a forgotten password.
[**end_user_authentications_passwords_patch**](EnduserauthenticationsApi.md#end_user_authentications_passwords_patch) | **PATCH** /end_user_authentications/passwords | 
[**end_user_authentications_post**](EnduserauthenticationsApi.md#end_user_authentications_post) | **POST** /end_user_authentications | Logs a user in.


# **end_user_authentication_users_post**
> PostEndUserAuthenticationResponse end_user_authentication_users_post(body => $body)

Create a new user.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::EnduserauthenticationsApi->new();
my $body = WWW::SwaggerClient::Object::CreateUser->new(); # CreateUser | 

eval { 
    my $result = $api_instance->end_user_authentication_users_post(body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling EnduserauthenticationsApi->end_user_authentication_users_post: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUser**](CreateUser.md)|  | 

### Return type

[**PostEndUserAuthenticationResponse**](PostEndUserAuthenticationResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **end_user_authentications_dates_get**
> GetEndUserAuthenticationsDatesResponse end_user_authentications_dates_get()

Gets an authoritative date_time string.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::EnduserauthenticationsApi->new();

eval { 
    my $result = $api_instance->end_user_authentications_dates_get();
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling EnduserauthenticationsApi->end_user_authentications_dates_get: $@\n";
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetEndUserAuthenticationsDatesResponse**](GetEndUserAuthenticationsDatesResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **end_user_authentications_delete**
> end_user_authentications_delete( => $, end_user_token => $end_user_token)

Logs a user out.

This logs a user out. the end-user-token will no longer be valid.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::EnduserauthenticationsApi->new();
my $ = '_example'; # string | The logged in user's token.
my $end_user_token = 'end_user_token_example'; # string | The logged in user's token.

eval { 
    $api_instance->end_user_authentications_delete( => $, end_user_token => $end_user_token);
};
if ($@) {
    warn "Exception when calling EnduserauthenticationsApi->end_user_authentications_delete: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | **string**| The logged in user&#39;s token. | 
 **end_user_token** | **string**| The logged in user&#39;s token. | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **end_user_authentications_get**
> GetEndUserAuthenticationsResponse end_user_authentications_get( => $, end_user_token => $end_user_token)

Get current authentication level for the user.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::EnduserauthenticationsApi->new();
my $ = '_example'; # string | The logged in user's token.
my $end_user_token = 'end_user_token_example'; # string | The logged in user's token.

eval { 
    my $result = $api_instance->end_user_authentications_get( => $, end_user_token => $end_user_token);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling EnduserauthenticationsApi->end_user_authentications_get: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | **string**| The logged in user&#39;s token. | 
 **end_user_token** | **string**| The logged in user&#39;s token. | 

### Return type

[**GetEndUserAuthenticationsResponse**](GetEndUserAuthenticationsResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **end_user_authentications_passwords_get**
> end_user_authentications_passwords_get(email => $email)

Request a forgotten password.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::EnduserauthenticationsApi->new();
my $email = 'email_example'; # string | The user e-mail to send a password to if valid.

eval { 
    $api_instance->end_user_authentications_passwords_get(email => $email);
};
if ($@) {
    warn "Exception when calling EnduserauthenticationsApi->end_user_authentications_passwords_get: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **string**| The user e-mail to send a password to if valid. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **end_user_authentications_passwords_patch**
> end_user_authentications_passwords_patch(body => $body, end_user_token => $end_user_token)



### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::EnduserauthenticationsApi->new();
my $body = WWW::SwaggerClient::Object::UpdatePassword->new(); # UpdatePassword | 
my $end_user_token = 'end_user_token_example'; # string | The logged in user's token.

eval { 
    $api_instance->end_user_authentications_passwords_patch(body => $body, end_user_token => $end_user_token);
};
if ($@) {
    warn "Exception when calling EnduserauthenticationsApi->end_user_authentications_passwords_patch: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdatePassword**](UpdatePassword.md)|  | 
 **end_user_token** | **string**| The logged in user&#39;s token. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **end_user_authentications_post**
> PostEndUserAuthenticationResponse end_user_authentications_post( => $, body => $body)

Logs a user in.

This function sends login credentials, and retrieves a stateless token.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::EnduserauthenticationsApi->new();
my $ = '_example'; # string | The logged in user's token.
my $body = WWW::SwaggerClient::Object::Login->new(); # Login | 

eval { 
    my $result = $api_instance->end_user_authentications_post( => $, body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling EnduserauthenticationsApi->end_user_authentications_post: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | **string**| The logged in user&#39;s token. | 
 **body** | [**Login**](Login.md)|  | 

### Return type

[**PostEndUserAuthenticationResponse**](PostEndUserAuthenticationResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

