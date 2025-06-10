# ChatCompletionRequestPublic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** | Unstructured or structured data type | [optional] 
**agent_flag** | **bool** | Flag to indicate if the request is for an agent | [optional] [default to False]
**agent_id** | **str** | ID of the agent to use for processing | [optional] 
**agent_strategy** | **str** | Strategy to use for agent processing | [optional] 
**agent_history_enabled** | **bool** | Flag to indicate if the agent history is enabled | [optional] [default to False]
**model** | **str** | Model ID | [optional] 
**knowledge_base** | [**KnowledgeBase**](KnowledgeBase.md) |  | [optional] 
**messages** | [**List[Message]**](Message.md) | List of conversation messages | 
**database_name** | **str** | Name of the database to use for structured processing for the &#39;structured&#39; strategy, default is &#39;all&#39; | [optional] 
**table_name** | **str** | Name of the table to use for structured processing for the &#39;structured&#39; strategy, not required to be passed in | [optional] 
**stream** | **bool** | Whether to stream responses | [optional] [default to False]
**max_trials** | **int** | Maximum number of trials for the agent | [optional] [default to 10]
**conversation_id** | **str** | Conversation ID to enable tracking of the conversation and recall and analytics | [optional] 
**request_id** | **str** | Request ID to enable tracking of the request, unique per request | [optional] 

## Example

```python
from verity_ai_pyc.models.chat_completion_request_public import ChatCompletionRequestPublic

# TODO update the JSON string below
json = "{}"
# create an instance of ChatCompletionRequestPublic from a JSON string
chat_completion_request_public_instance = ChatCompletionRequestPublic.from_json(json)
# print the JSON string representation of the object
print(ChatCompletionRequestPublic.to_json())

# convert the object into a dict
chat_completion_request_public_dict = chat_completion_request_public_instance.to_dict()
# create an instance of ChatCompletionRequestPublic from a dict
chat_completion_request_public_from_dict = ChatCompletionRequestPublic.from_dict(chat_completion_request_public_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


