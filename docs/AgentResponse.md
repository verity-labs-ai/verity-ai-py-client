# AgentResponse

Model for agent API responses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**model** | **str** |  | 
**system_prompt** | **str** |  | 
**custom_prompt** | **str** |  | 
**allowed_tools** | **List[str]** |  | 
**use_mcp** | **bool** |  | 
**mcp_server_urls** | **List[str]** |  | 
**agent_strategy** | **str** |  | 
**stream** | **bool** |  | 
**active** | **bool** |  | 
**version** | **str** |  | [optional] 
**organisation** | **str** |  | 
**agent_origin** | **str** | Origin type: &#39;preset&#39; or &#39;custom&#39; | 
**parent_agent_id** | **str** | ID of the parent preset agent if this is a custom agent derived from a preset | [optional] 
**knowledge_base** | **str** | Knowledge base the agent uses for unstructured data retrieval | [optional] 
**database_name** | **str** | Database name the agent uses for structured data queries | [optional] 
**table_name** | **str** | Table name the agent uses for structured data queries | [optional] 
**max_trials** | **int** | Maximum number of tool execution cycles | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from verity_ai_pyc.models.agent_response import AgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentResponse from a JSON string
agent_response_instance = AgentResponse.from_json(json)
# print the JSON string representation of the object
print(AgentResponse.to_json())

# convert the object into a dict
agent_response_dict = agent_response_instance.to_dict()
# create an instance of AgentResponse from a dict
agent_response_from_dict = AgentResponse.from_dict(agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


