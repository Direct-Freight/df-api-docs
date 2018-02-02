# WWW::SwaggerClient::PostingsApi

## Load the API package
```perl
use WWW::SwaggerClient::Object::PostingsApi;
```

All URIs are relative to *https://www.directfreight.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postings_custom_categories_category_type_delete**](PostingsApi.md#postings_custom_categories_category_type_delete) | **DELETE** /postings/custom_categories/{category_type} | Delete some or all custom columns, or custom_column data.
[**postings_custom_categories_category_type_get**](PostingsApi.md#postings_custom_categories_category_type_get) | **GET** /postings/custom_categories/{category_type} | Get a list of custom columns, or custom_column data.
[**postings_custom_categories_category_type_patch**](PostingsApi.md#postings_custom_categories_category_type_patch) | **PATCH** /postings/custom_categories/{category_type} | Update a category name, or value.
[**postings_custom_categories_category_type_post**](PostingsApi.md#postings_custom_categories_category_type_post) | **POST** /postings/custom_categories/{category_type} | Create new category names, or add new data.
[**postings_multiple_posting_type_post**](PostingsApi.md#postings_multiple_posting_type_post) | **POST** /postings/multiple/{posting_type} | Create, multiple entries at once. This is a convenience method.
[**postings_posting_type_action_post**](PostingsApi.md#postings_posting_type_action_post) | **POST** /postings/{posting_type}/{action} | Copy or Move an posting.
[**postings_posting_type_delete**](PostingsApi.md#postings_posting_type_delete) | **DELETE** /postings/{posting_type} | Remove one or more postings.
[**postings_posting_type_get**](PostingsApi.md#postings_posting_type_get) | **GET** /postings/{posting_type} | Get posts by this user.
[**postings_posting_type_patch**](PostingsApi.md#postings_posting_type_patch) | **PATCH** /postings/{posting_type} | Update an posting.
[**postings_posting_type_post**](PostingsApi.md#postings_posting_type_post) | **POST** /postings/{posting_type} | Copy or Move an posting.


# **postings_custom_categories_category_type_delete**
> postings_custom_categories_category_type_delete(category_type => $category_type, end_user_token => $end_user_token, category_id => $category_id)

Delete some or all custom columns, or custom_column data.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::PostingsApi->new();
my $category_type = 'category_type_example'; # string | Valid types are \"names\", and \"data\".
my $end_user_token = 'end_user_token_example'; # string | The logged in account's token.
my $category_id = (); # ARRAY[string] | To just delete information about some postings.

eval { 
    $api_instance->postings_custom_categories_category_type_delete(category_type => $category_type, end_user_token => $end_user_token, category_id => $category_id);
};
if ($@) {
    warn "Exception when calling PostingsApi->postings_custom_categories_category_type_delete: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_type** | **string**| Valid types are \&quot;names\&quot;, and \&quot;data\&quot;. | 
 **end_user_token** | **string**| The logged in account&#39;s token. | 
 **category_id** | [**ARRAY[string]**](string.md)| To just delete information about some postings. | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postings_custom_categories_category_type_get**
> GetCustomCategoriesResponse postings_custom_categories_category_type_get(end_user_token => $end_user_token, category_type => $category_type, category_id => $category_id)

Get a list of custom columns, or custom_column data.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::PostingsApi->new();
my $end_user_token = 'end_user_token_example'; # string | The logged in account's token.
my $category_type = 'category_type_example'; # string | Valid types are \"names\", and \"data\".
my $category_id = (); # ARRAY[string] | To just return information about some postings.

eval { 
    my $result = $api_instance->postings_custom_categories_category_type_get(end_user_token => $end_user_token, category_type => $category_type, category_id => $category_id);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling PostingsApi->postings_custom_categories_category_type_get: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_user_token** | **string**| The logged in account&#39;s token. | 
 **category_type** | **string**| Valid types are \&quot;names\&quot;, and \&quot;data\&quot;. | 
 **category_id** | [**ARRAY[string]**](string.md)| To just return information about some postings. | [optional] 

### Return type

[**GetCustomCategoriesResponse**](GetCustomCategoriesResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postings_custom_categories_category_type_patch**
> PostCustomCategoriesResponse postings_custom_categories_category_type_patch(category_type => $category_type, end_user_token => $end_user_token, body => $body)

Update a category name, or value.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::PostingsApi->new();
my $category_type = 'category_type_example'; # string | Valid types are \"names\", and \"data\".
my $end_user_token = 'end_user_token_example'; # string | The logged in account's token.
my $body = WWW::SwaggerClient::Object::UpdateCcInfo->new(); # UpdateCcInfo | 

eval { 
    my $result = $api_instance->postings_custom_categories_category_type_patch(category_type => $category_type, end_user_token => $end_user_token, body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling PostingsApi->postings_custom_categories_category_type_patch: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_type** | **string**| Valid types are \&quot;names\&quot;, and \&quot;data\&quot;. | 
 **end_user_token** | **string**| The logged in account&#39;s token. | 
 **body** | [**UpdateCcInfo**](UpdateCcInfo.md)|  | 

### Return type

[**PostCustomCategoriesResponse**](PostCustomCategoriesResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postings_custom_categories_category_type_post**
> PostCustomCategoriesResponse postings_custom_categories_category_type_post(category_type => $category_type, end_user_token => $end_user_token, body => $body)

Create new category names, or add new data.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::PostingsApi->new();
my $category_type = 'category_type_example'; # string | Valid types are \"names\", and \"data\".
my $end_user_token = 'end_user_token_example'; # string | The logged in account's token.
my $body = WWW::SwaggerClient::Object::CreateCcInfo->new(); # CreateCcInfo | 

eval { 
    my $result = $api_instance->postings_custom_categories_category_type_post(category_type => $category_type, end_user_token => $end_user_token, body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling PostingsApi->postings_custom_categories_category_type_post: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_type** | **string**| Valid types are \&quot;names\&quot;, and \&quot;data\&quot;. | 
 **end_user_token** | **string**| The logged in account&#39;s token. | 
 **body** | [**CreateCcInfo**](CreateCcInfo.md)|  | 

### Return type

[**PostCustomCategoriesResponse**](PostCustomCategoriesResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postings_multiple_posting_type_post**
> PostPostingMultipleResponse postings_multiple_posting_type_post(posting_type => $posting_type, end_user_token => $end_user_token, body => $body)

Create, multiple entries at once. This is a convenience method.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::PostingsApi->new();
my $posting_type = 'posting_type_example'; # string | Valid types are \"loads\", \"trucks\", \"private_loads\", \"private_trucks\", \"test_loads\", and \"test_trucks\"
my $end_user_token = 'end_user_token_example'; # string | The logged in account's token.
my $body = WWW::SwaggerClient::Object::CreateMultiplePostings->new(); # CreateMultiplePostings | 

eval { 
    my $result = $api_instance->postings_multiple_posting_type_post(posting_type => $posting_type, end_user_token => $end_user_token, body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling PostingsApi->postings_multiple_posting_type_post: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **posting_type** | **string**| Valid types are \&quot;loads\&quot;, \&quot;trucks\&quot;, \&quot;private_loads\&quot;, \&quot;private_trucks\&quot;, \&quot;test_loads\&quot;, and \&quot;test_trucks\&quot; | 
 **end_user_token** | **string**| The logged in account&#39;s token. | 
 **body** | [**CreateMultiplePostings**](CreateMultiplePostings.md)|  | 

### Return type

[**PostPostingMultipleResponse**](PostPostingMultipleResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postings_posting_type_action_post**
> PostPostingTypeActionResponse postings_posting_type_action_post(end_user_token => $end_user_token, posting_type => $posting_type, action => $action, body => $body)

Copy or Move an posting.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::PostingsApi->new();
my $end_user_token = 'end_user_token_example'; # string | The logged in account's token
my $posting_type = 'posting_type_example'; # string | Valid types are \"loads\", \"trucks\", \"private_loads\", \"private_trucks\", \"test_loads\", and \"test_trucks\"
my $action = 'action_example'; # string | Specified in the url. Valid types are \"copy\", and \"move\"
my $body = WWW::SwaggerClient::Object::PostPostingTypeActionBody->new(); # PostPostingTypeActionBody | 

eval { 
    my $result = $api_instance->postings_posting_type_action_post(end_user_token => $end_user_token, posting_type => $posting_type, action => $action, body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling PostingsApi->postings_posting_type_action_post: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_user_token** | **string**| The logged in account&#39;s token | 
 **posting_type** | **string**| Valid types are \&quot;loads\&quot;, \&quot;trucks\&quot;, \&quot;private_loads\&quot;, \&quot;private_trucks\&quot;, \&quot;test_loads\&quot;, and \&quot;test_trucks\&quot; | 
 **action** | **string**| Specified in the url. Valid types are \&quot;copy\&quot;, and \&quot;move\&quot; | 
 **body** | [**PostPostingTypeActionBody**](PostPostingTypeActionBody.md)|  | 

### Return type

[**PostPostingTypeActionResponse**](PostPostingTypeActionResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postings_posting_type_delete**
> postings_posting_type_delete(posting_type => $posting_type, end_user_token => $end_user_token, posting_id => $posting_id)

Remove one or more postings.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::PostingsApi->new();
my $posting_type = 'posting_type_example'; # string | Valid types are \"loads\", \"trucks\", \"private_loads\", \"private_trucks\", \"test_loads\", and \"test_trucks\"
my $end_user_token = 'end_user_token_example'; # string | The logged in account's token.
my $posting_id = (); # ARRAY[string] | You must specify which entry to remove.

eval { 
    $api_instance->postings_posting_type_delete(posting_type => $posting_type, end_user_token => $end_user_token, posting_id => $posting_id);
};
if ($@) {
    warn "Exception when calling PostingsApi->postings_posting_type_delete: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **posting_type** | **string**| Valid types are \&quot;loads\&quot;, \&quot;trucks\&quot;, \&quot;private_loads\&quot;, \&quot;private_trucks\&quot;, \&quot;test_loads\&quot;, and \&quot;test_trucks\&quot; | 
 **end_user_token** | **string**| The logged in account&#39;s token. | 
 **posting_id** | [**ARRAY[string]**](string.md)| You must specify which entry to remove. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postings_posting_type_get**
> GetPostingTypeResponse postings_posting_type_get(posting_type => $posting_type, end_user_token => $end_user_token, posting_id => $posting_id)

Get posts by this user.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::PostingsApi->new();
my $posting_type = 'posting_type_example'; # string | Valid types are \"loads\", \"trucks\", \"private_loads\", \"private_trucks\", \"test_loads\", and \"test_trucks\"
my $end_user_token = 'end_user_token_example'; # string | The logged in account's token.
my $posting_id = (); # ARRAY[string] | To just return information about some postings.

eval { 
    my $result = $api_instance->postings_posting_type_get(posting_type => $posting_type, end_user_token => $end_user_token, posting_id => $posting_id);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling PostingsApi->postings_posting_type_get: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **posting_type** | **string**| Valid types are \&quot;loads\&quot;, \&quot;trucks\&quot;, \&quot;private_loads\&quot;, \&quot;private_trucks\&quot;, \&quot;test_loads\&quot;, and \&quot;test_trucks\&quot; | 
 **end_user_token** | **string**| The logged in account&#39;s token. | 
 **posting_id** | [**ARRAY[string]**](string.md)| To just return information about some postings. | [optional] 

### Return type

[**GetPostingTypeResponse**](GetPostingTypeResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postings_posting_type_patch**
> GetPostingTypeResponse postings_posting_type_patch(posting_type => $posting_type, end_user_token => $end_user_token, body => $body)

Update an posting.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::PostingsApi->new();
my $posting_type = 'posting_type_example'; # string | Valid types are \"loads\", \"trucks\", \"private_loads\", \"private_trucks\", \"test_loads\", and \"test_trucks\"
my $end_user_token = 'end_user_token_example'; # string | The logged in account's token.
my $body = WWW::SwaggerClient::Object::PostObjectModel->new(); # PostObjectModel | 

eval { 
    my $result = $api_instance->postings_posting_type_patch(posting_type => $posting_type, end_user_token => $end_user_token, body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling PostingsApi->postings_posting_type_patch: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **posting_type** | **string**| Valid types are \&quot;loads\&quot;, \&quot;trucks\&quot;, \&quot;private_loads\&quot;, \&quot;private_trucks\&quot;, \&quot;test_loads\&quot;, and \&quot;test_trucks\&quot; | 
 **end_user_token** | **string**| The logged in account&#39;s token. | 
 **body** | [**PostObjectModel**](PostObjectModel.md)|  | [optional] 

### Return type

[**GetPostingTypeResponse**](GetPostingTypeResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postings_posting_type_post**
> object postings_posting_type_post(posting_type => $posting_type, end_user_token => $end_user_token, body => $body)

Copy or Move an posting.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::PostingsApi->new();
my $posting_type = 'posting_type_example'; # string | Valid types are \"loads\", \"trucks\", \"private_loads\", \"private_trucks\", \"test_loads\", and \"test_trucks\"
my $end_user_token = 'end_user_token_example'; # string | The logged in account's token.
my $body = WWW::SwaggerClient::Object::PostObjectModel->new(); # PostObjectModel | 

eval { 
    my $result = $api_instance->postings_posting_type_post(posting_type => $posting_type, end_user_token => $end_user_token, body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling PostingsApi->postings_posting_type_post: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **posting_type** | **string**| Valid types are \&quot;loads\&quot;, \&quot;trucks\&quot;, \&quot;private_loads\&quot;, \&quot;private_trucks\&quot;, \&quot;test_loads\&quot;, and \&quot;test_trucks\&quot; | 
 **end_user_token** | **string**| The logged in account&#39;s token. | 
 **body** | [**PostObjectModel**](PostObjectModel.md)|  | 

### Return type

**object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

