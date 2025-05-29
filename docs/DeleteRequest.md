# DeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filenames** | **List[str]** | List of filenames to delete | 

## Example

```python
from verity_ai_pyc.models.delete_request import DeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRequest from a JSON string
delete_request_instance = DeleteRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteRequest.to_json())

# convert the object into a dict
delete_request_dict = delete_request_instance.to_dict()
# create an instance of DeleteRequest from a dict
delete_request_from_dict = DeleteRequest.from_dict(delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


