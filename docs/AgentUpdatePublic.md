# AgentUpdatePublic

Public model for updating an existing agent - all fields optional

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**system_prompt** | **str** |  | [optional] 
**custom_prompt** | **str** |  | [optional] 
**allowed_tools** | **List[str]** |  | [optional] 
**use_mcp** | **bool** |  | [optional] 
**mcp_server_urls** | **List[str]** |  | [optional] 
**agent_strategy** | **str** |  | [optional] 
**stream** | **bool** |  | [optional] 
**active** | **bool** |  | [optional] 
**agent_origin** | **str** | Origin type: &#39;preset&#39; or &#39;custom&#39; | [optional] 
**parent_agent_id** | **str** | ID of the parent preset agent if this is a custom agent derived from a preset | [optional] 
**knowledge_base** | **str** | Knowledge base the agent should use for unstructured data retrieval | [optional] 
**database_name** | **str** | Database name the agent should use for structured data queries | [optional] 
**table_name** | **str** | Table name the agent should use for structured data queries | [optional] 
**max_trials** | **int** | Maximum number of tool execution cycles | [optional] 

## Example

```python
from verity_ai_pyc.models.agent_update_public import AgentUpdatePublic

# TODO update the JSON string below
json = "{}"
# create an instance of AgentUpdatePublic from a JSON string
agent_update_public_instance = AgentUpdatePublic.from_json(json)
# print the JSON string representation of the object
print(AgentUpdatePublic.to_json())

# convert the object into a dict
agent_update_public_dict = agent_update_public_instance.to_dict()
# create an instance of AgentUpdatePublic from a dict
agent_update_public_from_dict = AgentUpdatePublic.from_dict(agent_update_public_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


