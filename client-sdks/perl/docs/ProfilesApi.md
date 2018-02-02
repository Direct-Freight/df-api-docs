# WWW::SwaggerClient::ProfilesApi

## Load the API package
```perl
use WWW::SwaggerClient::Object::ProfilesApi;
```

All URIs are relative to *https://www.directfreight.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**profiles_documents_delete**](ProfilesApi.md#profiles_documents_delete) | **DELETE** /profiles/documents | Delete the document.
[**profiles_documents_get**](ProfilesApi.md#profiles_documents_get) | **GET** /profiles/documents | Retrieve documents
[**profiles_documents_patch**](ProfilesApi.md#profiles_documents_patch) | **PATCH** /profiles/documents | Rename a document.
[**profiles_documents_post**](ProfilesApi.md#profiles_documents_post) | **POST** /profiles/documents | Upload a new document.
[**profiles_get**](ProfilesApi.md#profiles_get) | **GET** /profiles | Request the logged in user&#39;s profile.
[**profiles_mobile_carriers_get**](ProfilesApi.md#profiles_mobile_carriers_get) | **GET** /profiles/mobile_carriers | Retrieve one or more mobile carriers. 
[**profiles_optins_delete**](ProfilesApi.md#profiles_optins_delete) | **DELETE** /profiles/optins | Marks the profile as opted out.
[**profiles_optins_get**](ProfilesApi.md#profiles_optins_get) | **GET** /profiles/optins | Check if the profile has opted to being contacted by text.
[**profiles_optins_patch**](ProfilesApi.md#profiles_optins_patch) | **PATCH** /profiles/optins | Marks the profile as opted in.
[**profiles_optins_post**](ProfilesApi.md#profiles_optins_post) | **POST** /profiles/optins | Create, and send an Optin Code.
[**profiles_patch**](ProfilesApi.md#profiles_patch) | **PATCH** /profiles | Update profile information.
[**profiles_post**](ProfilesApi.md#profiles_post) | **POST** /profiles | Create a new profile.


# **profiles_documents_delete**
> profiles_documents_delete(end_user_token => $end_user_token)

Delete the document.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::ProfilesApi->new();
my $end_user_token = 'end_user_token_example'; # string | The logged in profile's token.

eval { 
    $api_instance->profiles_documents_delete(end_user_token => $end_user_token);
};
if ($@) {
    warn "Exception when calling ProfilesApi->profiles_documents_delete: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_user_token** | **string**| The logged in profile&#39;s token. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_documents_get**
> profiles_documents_get(end_user_token => $end_user_token)

Retrieve documents

Retrieve documents

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::ProfilesApi->new();
my $end_user_token = 'end_user_token_example'; # string | The logged in profile's token.

eval { 
    $api_instance->profiles_documents_get(end_user_token => $end_user_token);
};
if ($@) {
    warn "Exception when calling ProfilesApi->profiles_documents_get: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_user_token** | **string**| The logged in profile&#39;s token. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_documents_patch**
> profiles_documents_patch(end_user_token => $end_user_token, body => $body)

Rename a document.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::ProfilesApi->new();
my $end_user_token = 'end_user_token_example'; # string | The logged in profile's token.
my $body = WWW::SwaggerClient::Object::RenameDocument->new(); # RenameDocument | 

eval { 
    $api_instance->profiles_documents_patch(end_user_token => $end_user_token, body => $body);
};
if ($@) {
    warn "Exception when calling ProfilesApi->profiles_documents_patch: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_user_token** | **string**| The logged in profile&#39;s token. | 
 **body** | [**RenameDocument**](RenameDocument.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_documents_post**
> SuccessSuccessResponse profiles_documents_post(end_user_token => $end_user_token, body => $body)

Upload a new document.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::ProfilesApi->new();
my $end_user_token = 'end_user_token_example'; # string | The logged in profile's token.
my $body = WWW::SwaggerClient::Object::UploadDocument->new(); # UploadDocument | 

eval { 
    my $result = $api_instance->profiles_documents_post(end_user_token => $end_user_token, body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling ProfilesApi->profiles_documents_post: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_user_token** | **string**| The logged in profile&#39;s token. | 
 **body** | [**UploadDocument**](UploadDocument.md)|  | 

### Return type

[**SuccessSuccessResponse**](SuccessSuccessResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_get**
> ProfileModel profiles_get(end_user_token => $end_user_token)

Request the logged in user's profile.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::ProfilesApi->new();
my $end_user_token = 'end_user_token_example'; # string | The logged in profile's token.

eval { 
    my $result = $api_instance->profiles_get(end_user_token => $end_user_token);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling ProfilesApi->profiles_get: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_user_token** | **string**| The logged in profile&#39;s token. | 

### Return type

[**ProfileModel**](ProfileModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_mobile_carriers_get**
> MobileCarrierResponse profiles_mobile_carriers_get(body => $body)

Retrieve one or more mobile carriers. 

Retrieve a list of supported carriers.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::ProfilesApi->new();
my $body = WWW::SwaggerClient::Object::GetMobileCarrierBody->new(); # GetMobileCarrierBody | A way to just get back the info for just one carrier.

eval { 
    my $result = $api_instance->profiles_mobile_carriers_get(body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling ProfilesApi->profiles_mobile_carriers_get: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetMobileCarrierBody**](GetMobileCarrierBody.md)| A way to just get back the info for just one carrier. | 

### Return type

[**MobileCarrierResponse**](MobileCarrierResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_optins_delete**
> profiles_optins_delete(end_user_token => $end_user_token)

Marks the profile as opted out.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::ProfilesApi->new();
my $end_user_token = 'end_user_token_example'; # string | The logged in profile's token.

eval { 
    $api_instance->profiles_optins_delete(end_user_token => $end_user_token);
};
if ($@) {
    warn "Exception when calling ProfilesApi->profiles_optins_delete: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_user_token** | **string**| The logged in profile&#39;s token. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_optins_get**
> SuccessStatusResponse profiles_optins_get(end_user_token => $end_user_token)

Check if the profile has opted to being contacted by text.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::ProfilesApi->new();
my $end_user_token = 'end_user_token_example'; # string | The logged in profile's token.

eval { 
    my $result = $api_instance->profiles_optins_get(end_user_token => $end_user_token);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling ProfilesApi->profiles_optins_get: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_user_token** | **string**| The logged in profile&#39;s token. | 

### Return type

[**SuccessStatusResponse**](SuccessStatusResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_optins_patch**
> SuccessSuccessResponse profiles_optins_patch(end_user_token => $end_user_token)

Marks the profile as opted in.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::ProfilesApi->new();
my $end_user_token = 'end_user_token_example'; # string | The logged in profile's token.

eval { 
    my $result = $api_instance->profiles_optins_patch(end_user_token => $end_user_token);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling ProfilesApi->profiles_optins_patch: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_user_token** | **string**| The logged in profile&#39;s token. | 

### Return type

[**SuccessSuccessResponse**](SuccessSuccessResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_optins_post**
> PostOptinCodeResponse profiles_optins_post(end_user_token => $end_user_token)

Create, and send an Optin Code.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::ProfilesApi->new();
my $end_user_token = 'end_user_token_example'; # string | The logged in profile's token.

eval { 
    my $result = $api_instance->profiles_optins_post(end_user_token => $end_user_token);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling ProfilesApi->profiles_optins_post: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_user_token** | **string**| The logged in profile&#39;s token. | 

### Return type

[**PostOptinCodeResponse**](PostOptinCodeResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_patch**
> ProfileModel profiles_patch(end_user_token => $end_user_token, body => $body)

Update profile information.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::ProfilesApi->new();
my $end_user_token = 'end_user_token_example'; # string | The logged in profile's token.
my $body = WWW::SwaggerClient::Object::PatchProfile->new(); # PatchProfile | 

eval { 
    my $result = $api_instance->profiles_patch(end_user_token => $end_user_token, body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling ProfilesApi->profiles_patch: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_user_token** | **string**| The logged in profile&#39;s token. | 
 **body** | [**PatchProfile**](PatchProfile.md)|  | 

### Return type

[**ProfileModel**](ProfileModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_post**
> SuccessSuccessResponse profiles_post(end_user_token => $end_user_token, body => $body)

Create a new profile.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::ProfilesApi->new();
my $end_user_token = 'end_user_token_example'; # string | The logged in profile's token.
my $body = WWW::SwaggerClient::Object::CreateProfile->new(); # CreateProfile | 

eval { 
    my $result = $api_instance->profiles_post(end_user_token => $end_user_token, body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling ProfilesApi->profiles_post: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_user_token** | **string**| The logged in profile&#39;s token. | 
 **body** | [**CreateProfile**](CreateProfile.md)|  | 

### Return type

[**SuccessSuccessResponse**](SuccessSuccessResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

