# WWW::SwaggerClient::Object::SearchBoard

## Load the model package
```perl
use WWW::SwaggerClient::Object::SearchBoard;
```

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_id** | **boolean** | By specifying an alert_id we will record the loads seen by this user, and associate it with their alert.  | [optional] 
**count** | **boolean** | If included this will return a count instead of a list.  | [optional] 
**destination_city** | **string** | Must be at least 2 characters.  | [optional] 
**destination_radius** | **int** | If both city and state, it will search for all entries within # Miles of the city.  | [optional] 
**destination_state** | **ARRAY[string]** | If it is an array, we assume a multi state search, and ignore destination_city.  | [optional] 
**item_count** | **int** | Will default to 50 items per page. Max is 100, minimum is 1.  | [optional] 
**load_size** | **ARRAY[string]** | This is only valid on load boards. Valid values are &amp;quot;Full&amp;quot; and &amp;quot;Partial&amp;quot;.  | [optional] 
**only_new** | **boolean** | This will only return unseen results. This requires an alert_id to be specified.  | [optional] 
**origin_city** | **string** | Must be at least 3 characters.  | [optional] 
**origin_radius** | **int** | If both city and state, it will search for all entries within # Miles of the city.  | [optional] 
**origin_state** | **ARRAY[string]** | If it is an array, we assume a multi state search, and ignore origin_city.  | 
**page_number** | **int** | The page you are on.  | 
**ship_date** | **ARRAY[string]** | Limit the board to only show loads with X ship date.  | [optional] 
**total_items** | **int** | A count of all the entry objects for the specified search.  | 
**total_pages** | **int** | A count of the # of pages based on the search parameters.  | 
**trailer_type** | **ARRAY[string]** | A string array of valid trailer types to limit the search.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


