# WWW::SwaggerClient::LocationsApi

## Load the API package
```perl
use WWW::SwaggerClient::Object::LocationsApi;
```

All URIs are relative to *https://www.directfreight.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**location_distance_get**](LocationsApi.md#location_distance_get) | **GET** /location/distance | Get the distance between 2 locations. This is used to calculate dead head miles.
[**locations_closest_city_get**](LocationsApi.md#locations_closest_city_get) | **GET** /locations/closest_city | Will return the closest city to a lat/lon point.
[**locations_partial_match_get**](LocationsApi.md#locations_partial_match_get) | **GET** /locations/partial_match | A string of a partial city or state name, and returns a list of possible matches.


# **location_distance_get**
> GetLocationDistanceResponse location_distance_get(origin_city => $origin_city, origin_state => $origin_state, destination_city => $destination_city, destination_state => $destination_state)

Get the distance between 2 locations. This is used to calculate dead head miles.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::LocationsApi->new();
my $origin_city = 'origin_city_example'; # string | 
my $origin_state = 'origin_state_example'; # string | 
my $destination_city = 'destination_city_example'; # string | 
my $destination_state = 'destination_state_example'; # string | 

eval { 
    my $result = $api_instance->location_distance_get(origin_city => $origin_city, origin_state => $origin_state, destination_city => $destination_city, destination_state => $destination_state);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling LocationsApi->location_distance_get: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin_city** | **string**|  | 
 **origin_state** | **string**|  | 
 **destination_city** | **string**|  | 
 **destination_state** | **string**|  | 

### Return type

[**GetLocationDistanceResponse**](GetLocationDistanceResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_closest_city_get**
> GetClosestCityResponse locations_closest_city_get(latitude => $latitude, longitude => $longitude)

Will return the closest city to a lat/lon point.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::LocationsApi->new();
my $latitude = 3.4; # double | 
my $longitude = 3.4; # double | 

eval { 
    my $result = $api_instance->locations_closest_city_get(latitude => $latitude, longitude => $longitude);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling LocationsApi->locations_closest_city_get: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **latitude** | **double**|  | 
 **longitude** | **double**|  | 

### Return type

[**GetClosestCityResponse**](GetClosestCityResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_partial_match_get**
> locations_partial_match_get(term => $term, search_type => $search_type)

A string of a partial city or state name, and returns a list of possible matches.

### Example 
```perl
use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::LocationsApi->new();
my $term = 'term_example'; # string | Min 2 characters.
my $search_type = 'search_type_example'; # string | \"state\", and \"city\" will return only returns only the respective information for that search type. Misspelling, will default to city.

eval { 
    $api_instance->locations_partial_match_get(term => $term, search_type => $search_type);
};
if ($@) {
    warn "Exception when calling LocationsApi->locations_partial_match_get: $@\n";
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **string**| Min 2 characters. | 
 **search_type** | **string**| \&quot;state\&quot;, and \&quot;city\&quot; will return only returns only the respective information for that search type. Misspelling, will default to city. | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

