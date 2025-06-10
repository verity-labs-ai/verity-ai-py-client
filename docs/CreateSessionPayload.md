# CreateSessionPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**email** | **str** |  | 

## Example

```python
from verity_ai_pyc.models.create_session_payload import CreateSessionPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSessionPayload from a JSON string
create_session_payload_instance = CreateSessionPayload.from_json(json)
# print the JSON string representation of the object
print(CreateSessionPayload.to_json())

# convert the object into a dict
create_session_payload_dict = create_session_payload_instance.to_dict()
# create an instance of CreateSessionPayload from a dict
create_session_payload_from_dict = CreateSessionPayload.from_dict(create_session_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


