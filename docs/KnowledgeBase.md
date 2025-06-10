# KnowledgeBase

Name of the knowledge base to use for unstructured processing, default is 'all'. Can be a string or list of strings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from verity_ai_pyc.models.knowledge_base import KnowledgeBase

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBase from a JSON string
knowledge_base_instance = KnowledgeBase.from_json(json)
# print the JSON string representation of the object
print(KnowledgeBase.to_json())

# convert the object into a dict
knowledge_base_dict = knowledge_base_instance.to_dict()
# create an instance of KnowledgeBase from a dict
knowledge_base_from_dict = KnowledgeBase.from_dict(knowledge_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


