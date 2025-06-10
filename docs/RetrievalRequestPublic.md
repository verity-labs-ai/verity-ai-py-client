# RetrievalRequestPublic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | The user query to retrieve documents for. | 
**top_k** | **int** | The number of top documents to retrieve (5-10). | [optional] [default to 5]
**knowledge_base** | [**KnowledgeBase1**](KnowledgeBase1.md) |  | [optional] 

## Example

```python
from verity_ai_pyc.models.retrieval_request_public import RetrievalRequestPublic

# TODO update the JSON string below
json = "{}"
# create an instance of RetrievalRequestPublic from a JSON string
retrieval_request_public_instance = RetrievalRequestPublic.from_json(json)
# print the JSON string representation of the object
print(RetrievalRequestPublic.to_json())

# convert the object into a dict
retrieval_request_public_dict = retrieval_request_public_instance.to_dict()
# create an instance of RetrievalRequestPublic from a dict
retrieval_request_public_from_dict = RetrievalRequestPublic.from_dict(retrieval_request_public_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


