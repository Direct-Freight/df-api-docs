# WWW::SwaggerClient::BoardsApi

## Load the API package
```perl
use WWW::SwaggerClient::Object::BoardsApi;
```

All URIs are relative to *https://www.directfreight.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**boards_board_type_origin_state_origin_city_origin_radius_load_type_destination_state_destination_city_get**](BoardsApi.md#boards_board_type_origin_state_origin_city_origin_radius_load_type_destination_state_destination_city_get) | **GET** /boards/{board_type}/{origin_state}/{origin_city}/{origin_radius}/{load_type}/{destination_state}/{destination_city} | A convenience method for simple searches.
[**boards_board_type_post**](BoardsApi.md#boards_board_type_post) | **POST** /boards/{board_type} | Get a board.
[**boards_board_type_state_list_get**](BoardsApi.md#boards_board_type_state_list_get) | **GET** /boards/{board_type}/state_list | A convenience method to get totals by state.
[**boards_hidden_companies_delete**](BoardsApi.md#boards_hidden_companies_delete) | **DELETE** /boards/hidden_companies | Mark a company as not hidden.
[**boards_hidden_companies_get**](BoardsApi.md#boards_hidden_companies_get) | **GET** /boards/hidden_companies | Get a list of companies that should be hidden.
[**boards_hidden_companies_patch**](BoardsApi.md#boards_hidden_companies_patch) | **PATCH** /boards/hidden_companies | Toggle one or more company between hidden and unhidden.
[**boards_hidden_companies_post**](BoardsApi.md#boards_hidden_companies_post) | **POST** /boards/hidden_companies | Mark a set of companies as hidden.
[**boards_hidden_entries_delete**](BoardsApi.md#boards_hidden_entries_delete) | **DELETE** /boards/hidden_entries | Mark a set of entries as not hidden.
[**boards_hidden_entries_get**](BoardsApi.md#boards_hidden_entries_get) | **GET** /boards/hidden_entries | Get a list of entries that should be hidden.
[**boards_hidden_entries_patch**](BoardsApi.md#boards_hidden_entries_patch) | **PATCH** /boards/hidden_entries | Toggle one or more entry between hidden and unhidden.
[**boards_hidden_entries_post**](BoardsApi.md#boards_hidden_entries_post) | **POST** /boards/hidden_entries | Mark a set of entries as hidden.
[**boards_notes_delete**](BoardsApi.md#boards_notes_delete) | **DELETE** /boards/notes | Delete a note.
[**boards_notes_get**](BoardsApi.md#boards_notes_get) | **GET** /boards/notes | Get notes that this user has written.
[**boards_notes_patch**](BoardsApi.md#boards_notes_patch) | **PATCH** /boards/notes | Update a note.
[**boards_notes_post**](BoardsApi.md#boards_notes_post) | **POST** /boards/notes | Create a new note.


# **boards_board_type_origin_state_origin_city_origin_radius_load_type_destination_state_destination_city_get**
> PostBoardTypeResponse boards_board_type_origin_state_origin_city_origin_radius_load_type_destination_state_destination_city_get(board_type => $board_type, origin_state => $origin_state, origin_city => $origin_city, origin_radius => $origin_radius, destination_state => $destination_state, destination_city => $destination_city, load_type => $load_type, end_user_token => $end_user_token)

A convenience method for simple searches.

This is a convenience method. In the background it is calling the POST method. Refer to that method for more in-depth information.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::BoardsApi->new();
my $board_type = 'board_type_example'; # string | This will be specified in the url. Valid types are \"loads\", and \"trucks\".
my $origin_state = 'origin_state_example'; # string | The minimum needed for a search.
my $origin_city = 'origin_city_example'; # string | Must be at least 2 characters.
my $origin_radius = 56; # int | If both city and state, it will search for all entries within # Miles of the city.
my $destination_state = 'destination_state_example'; # string | If it is an array, we assume a multi state search, and ignore destination_city.
my $destination_city = 'destination_city_example'; # string | Must be at least 2 characters.
my $load_type = 'load_type_example'; # string | A string of comma separated valid trailer types to limit the search.
my $end_user_token = 'end_user_token_example'; # string | Sensitive info like phone numbers won't be returned without this.

eval { 
    my $result = $api_instance->boards_board_type_origin_state_origin_city_origin_radius_load_type_destination_state_destination_city_get(board_type => $board_type, origin_state => $origin_state, origin_city => $origin_city, origin_radius => $origin_radius, destination_state => $destination_state, destination_city => $destination_city, load_type => $load_type, end_user_token => $end_user_token);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling BoardsApi->boards_board_type_origin_state_origin_city_origin_radius_load_type_destination_state_destination_city_get: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **board_type** | **string**| This will be specified in the url. Valid types are \&quot;loads\&quot;, and \&quot;trucks\&quot;. | 
 **origin_state** | **string**| The minimum needed for a search. | 
 **origin_city** | **string**| Must be at least 2 characters. | 
 **origin_radius** | **int**| If both city and state, it will search for all entries within # Miles of the city. | 
 **destination_state** | **string**| If it is an array, we assume a multi state search, and ignore destination_city. | 
 **destination_city** | **string**| Must be at least 2 characters. | 
 **load_type** | **string**| A string of comma separated valid trailer types to limit the search. | 
 **end_user_token** | **string**| Sensitive info like phone numbers won&#39;t be returned without this. | [optional] 

### Return type

[**PostBoardTypeResponse**](PostBoardTypeResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_board_type_post**
> PostBoardTypeResponse boards_board_type_post(body => $body, board_type => $board_type, end_user_token => $end_user_token)

Get a board.

This is the primary search method.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::BoardsApi->new();
my $body = WWW::SwaggerClient::Object::SearchBoard->new(); # SearchBoard | 
my $board_type = 'board_type_example'; # string | This will be specified in the url. Valid types are \"loads\", and \"trucks\".
my $end_user_token = 'end_user_token_example'; # string | Sensitive info like phone numbers won't be returned without this.

eval { 
    my $result = $api_instance->boards_board_type_post(body => $body, board_type => $board_type, end_user_token => $end_user_token);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling BoardsApi->boards_board_type_post: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchBoard**](SearchBoard.md)|  | 
 **board_type** | **string**| This will be specified in the url. Valid types are \&quot;loads\&quot;, and \&quot;trucks\&quot;. | 
 **end_user_token** | **string**| Sensitive info like phone numbers won&#39;t be returned without this. | [optional] 

### Return type

[**PostBoardTypeResponse**](PostBoardTypeResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_board_type_state_list_get**
> GetStateListResponse boards_board_type_state_list_get(board_type => $board_type)

A convenience method to get totals by state.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::BoardsApi->new();
my $board_type = 'board_type_example'; # string | This will be specified in the url. Valid types are \"loads\", and \"trucks\".

eval { 
    my $result = $api_instance->boards_board_type_state_list_get(board_type => $board_type);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling BoardsApi->boards_board_type_state_list_get: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **board_type** | **string**| This will be specified in the url. Valid types are \&quot;loads\&quot;, and \&quot;trucks\&quot;. | 

### Return type

[**GetStateListResponse**](GetStateListResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_hidden_companies_delete**
> boards_hidden_companies_delete(end_user_token => $end_user_token, company_id => $company_id)

Mark a company as not hidden.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::BoardsApi->new();
my $end_user_token = 'end_user_token_example'; # string | Only logged in users can use this feature.
my $company_id = 'company_id_example'; # string | The company that need to be marked as not hidden.

eval { 
    $api_instance->boards_hidden_companies_delete(end_user_token => $end_user_token, company_id => $company_id);
};
if ($@) {
    warn "Exception when calling BoardsApi->boards_hidden_companies_delete: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_user_token** | **string**| Only logged in users can use this feature. | 
 **company_id** | **string**| The company that need to be marked as not hidden. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_hidden_companies_get**
> GetHiddenCompaniesResponse boards_hidden_companies_get(end_user_token => $end_user_token, company_name => $company_name)

Get a list of companies that should be hidden.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::BoardsApi->new();
my $end_user_token = 'end_user_token_example'; # string | Only logged in users can use this feature.
my $company_name = (); # ARRAY[string] | A list of id's to check if any should be visually hidden.

eval { 
    my $result = $api_instance->boards_hidden_companies_get(end_user_token => $end_user_token, company_name => $company_name);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling BoardsApi->boards_hidden_companies_get: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_user_token** | **string**| Only logged in users can use this feature. | 
 **company_name** | [**ARRAY[string]**](string.md)| A list of id&#39;s to check if any should be visually hidden. | 

### Return type

[**GetHiddenCompaniesResponse**](GetHiddenCompaniesResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_hidden_companies_patch**
> boards_hidden_companies_patch(end_user_token => $end_user_token, body => $body)

Toggle one or more company between hidden and unhidden.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::BoardsApi->new();
my $end_user_token = 'end_user_token_example'; # string | Only logged in users can use this feature.
my $body = WWW::SwaggerClient::Object::ToggleHiddenCompanies->new(); # ToggleHiddenCompanies | 

eval { 
    $api_instance->boards_hidden_companies_patch(end_user_token => $end_user_token, body => $body);
};
if ($@) {
    warn "Exception when calling BoardsApi->boards_hidden_companies_patch: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_user_token** | **string**| Only logged in users can use this feature. | 
 **body** | [**ToggleHiddenCompanies**](ToggleHiddenCompanies.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_hidden_companies_post**
> PostHiddenCompaniesResponse boards_hidden_companies_post(end_user_token => $end_user_token, body => $body)

Mark a set of companies as hidden.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::BoardsApi->new();
my $end_user_token = 'end_user_token_example'; # string | Only logged in users can use this feature.
my $body = WWW::SwaggerClient::Object::MarkHiddenCompanies->new(); # MarkHiddenCompanies | 

eval { 
    my $result = $api_instance->boards_hidden_companies_post(end_user_token => $end_user_token, body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling BoardsApi->boards_hidden_companies_post: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_user_token** | **string**| Only logged in users can use this feature. | 
 **body** | [**MarkHiddenCompanies**](MarkHiddenCompanies.md)|  | 

### Return type

[**PostHiddenCompaniesResponse**](PostHiddenCompaniesResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_hidden_entries_delete**
> boards_hidden_entries_delete(end_user_token => $end_user_token, entry_id => $entry_id)

Mark a set of entries as not hidden.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::BoardsApi->new();
my $end_user_token = 'end_user_token_example'; # string | Only logged in users can use this feature.
my $entry_id = 'entry_id_example'; # string | The entry that need to be marked as not hidden. 

eval { 
    $api_instance->boards_hidden_entries_delete(end_user_token => $end_user_token, entry_id => $entry_id);
};
if ($@) {
    warn "Exception when calling BoardsApi->boards_hidden_entries_delete: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_user_token** | **string**| Only logged in users can use this feature. | 
 **entry_id** | **string**| The entry that need to be marked as not hidden.  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_hidden_entries_get**
> GetHiddenEntries boards_hidden_entries_get(end_user_token => $end_user_token, entry_id => $entry_id)

Get a list of entries that should be hidden.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::BoardsApi->new();
my $end_user_token = 'end_user_token_example'; # string | Only logged in users can use this feature.
my $entry_id = (); # ARRAY[string] | A list of id's to check if any should be visually hidden.

eval { 
    my $result = $api_instance->boards_hidden_entries_get(end_user_token => $end_user_token, entry_id => $entry_id);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling BoardsApi->boards_hidden_entries_get: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_user_token** | **string**| Only logged in users can use this feature. | 
 **entry_id** | [**ARRAY[string]**](string.md)| A list of id&#39;s to check if any should be visually hidden. | 

### Return type

[**GetHiddenEntries**](GetHiddenEntries.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_hidden_entries_patch**
> boards_hidden_entries_patch(end_user_token => $end_user_token, body => $body)

Toggle one or more entry between hidden and unhidden.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::BoardsApi->new();
my $end_user_token = 'end_user_token_example'; # string | Only logged in users can use this feature.
my $body = WWW::SwaggerClient::Object::ToggleHiddenEntries->new(); # ToggleHiddenEntries | 

eval { 
    $api_instance->boards_hidden_entries_patch(end_user_token => $end_user_token, body => $body);
};
if ($@) {
    warn "Exception when calling BoardsApi->boards_hidden_entries_patch: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_user_token** | **string**| Only logged in users can use this feature. | 
 **body** | [**ToggleHiddenEntries**](ToggleHiddenEntries.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_hidden_entries_post**
> PostHiddenEntriesResponse boards_hidden_entries_post(end_user_token => $end_user_token, body => $body)

Mark a set of entries as hidden.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::BoardsApi->new();
my $end_user_token = 'end_user_token_example'; # string | Only logged in users can use this feature.
my $body = WWW::SwaggerClient::Object::MarkHiddenEntries->new(); # MarkHiddenEntries | 

eval { 
    my $result = $api_instance->boards_hidden_entries_post(end_user_token => $end_user_token, body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling BoardsApi->boards_hidden_entries_post: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_user_token** | **string**| Only logged in users can use this feature. | 
 **body** | [**MarkHiddenEntries**](MarkHiddenEntries.md)|  | 

### Return type

[**PostHiddenEntriesResponse**](PostHiddenEntriesResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_notes_delete**
> DeleteBoardsNotesResponse boards_notes_delete(end_user_token => $end_user_token, note_id => $note_id)

Delete a note.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::BoardsApi->new();
my $end_user_token = 'end_user_token_example'; # string | Only logged in users can use this feature.
my $note_id = 'note_id_example'; # string | The entry to associate the note with. 

eval { 
    my $result = $api_instance->boards_notes_delete(end_user_token => $end_user_token, note_id => $note_id);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling BoardsApi->boards_notes_delete: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_user_token** | **string**| Only logged in users can use this feature. | 
 **note_id** | **string**| The entry to associate the note with.  | 

### Return type

[**DeleteBoardsNotesResponse**](DeleteBoardsNotesResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_notes_get**
> GetBoardsNotesResponse boards_notes_get(end_user_token => $end_user_token, entry_id => $entry_id)

Get notes that this user has written.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::BoardsApi->new();
my $end_user_token = 'end_user_token_example'; # string | Only logged in users can use this feature.
my $entry_id = (); # ARRAY[string] | Optionally just check if certain loads have notes associated with them. 

eval { 
    my $result = $api_instance->boards_notes_get(end_user_token => $end_user_token, entry_id => $entry_id);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling BoardsApi->boards_notes_get: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_user_token** | **string**| Only logged in users can use this feature. | 
 **entry_id** | [**ARRAY[string]**](string.md)| Optionally just check if certain loads have notes associated with them.  | [optional] 

### Return type

[**GetBoardsNotesResponse**](GetBoardsNotesResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_notes_patch**
> PatchBoardsNotesResponse boards_notes_patch(end_user_token => $end_user_token, body => $body)

Update a note.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::BoardsApi->new();
my $end_user_token = 'end_user_token_example'; # string | Only logged in users can use this feature.
my $body = WWW::SwaggerClient::Object::UpdateNotes->new(); # UpdateNotes | 

eval { 
    my $result = $api_instance->boards_notes_patch(end_user_token => $end_user_token, body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling BoardsApi->boards_notes_patch: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_user_token** | **string**| Only logged in users can use this feature. | 
 **body** | [**UpdateNotes**](UpdateNotes.md)|  | 

### Return type

[**PatchBoardsNotesResponse**](PatchBoardsNotesResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_notes_post**
> PostBoardsNotesResponse boards_notes_post(end_user_token => $end_user_token, body => $body)

Create a new note.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::BoardsApi->new();
my $end_user_token = 'end_user_token_example'; # string | Only logged in users can use this feature.
my $body = WWW::SwaggerClient::Object::CreateNotes->new(); # CreateNotes | 

eval { 
    my $result = $api_instance->boards_notes_post(end_user_token => $end_user_token, body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling BoardsApi->boards_notes_post: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_user_token** | **string**| Only logged in users can use this feature. | 
 **body** | [**CreateNotes**](CreateNotes.md)|  | 

### Return type

[**PostBoardsNotesResponse**](PostBoardsNotesResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

