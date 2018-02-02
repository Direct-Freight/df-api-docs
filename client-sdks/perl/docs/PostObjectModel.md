# WWW::SwaggerClient::Object::PostObjectModel

## Load the model package
```perl
use WWW::SwaggerClient::Object::PostObjectModel;
```

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **object** |  | [optional] 
**custom_id** | **object** | A unique identifier a user can provide for their own records. | [optional] 
**destination_city** | **object** | For truck type entries this is optional. | [optional] 
**destination_state** | **object** | For truck type entries this is optional. | [optional] 
**height** | **object** |  | [optional] 
**length** | **object** |  | [optional] 
**load_size** | **object** | Require for load type entries only. This field expects one of the 2 following terms, full or partial. | [optional] 
**origin_city** | **object** | Required for all entry types. | 
**origin_state** | **object** | Required, 2 character limit. | 
**other_trailer_types** | **object** | This may be empty. | [optional] 
**pay_rate** | **object** |  | [optional] 
**posting_id** | **int** | A unique id in our system for the user&#39;s entry. | 
**receive_date** | **object** |  | [optional] 
**ship_date** | **object** |  | 
**trailer_type** | **object** | This can have 1 or more standard trailer types. | 
**weight** | **object** |  | [optional] 
**width** | **object** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


