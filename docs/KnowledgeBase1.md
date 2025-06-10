# KnowledgeBase1

The knowledge base context for the query. Default is 'all'. Can be a string or list of strings. In case specific knowledge bases are required use /kb endpoint to get the list of knowledge bases.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from verity_ai_pyc.models.knowledge_base1 import KnowledgeBase1

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBase1 from a JSON string
knowledge_base1_instance = KnowledgeBase1.from_json(json)
# print the JSON string representation of the object
print(KnowledgeBase1.to_json())

# convert the object into a dict
knowledge_base1_dict = knowledge_base1_instance.to_dict()
# create an instance of KnowledgeBase1 from a dict
knowledge_base1_from_dict = KnowledgeBase1.from_dict(knowledge_base1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


