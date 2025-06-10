# AgentCreatePublic

Public model for creating a new agent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the agent | 
**description** | **str** | Description of the agent&#39;s purpose and capabilities | [optional] 
**model** | **str** | LLM model identifier (e.g., &#39;anthropic_claude_3_5_sonnet_v1&#39;) | [optional] [default to 'anthropic_claude_3_5_sonnet_v1']
**system_prompt** | **str** | System prompt that defines the agent&#39;s behavior and context | [optional] 
**custom_prompt** | **str** | Custom prompt that can be used to add additional instructions to the agent | [optional] 
**knowledge_base** | **str** | Knowledge base the agent should use for unstructured data retrieval | [optional] 
**database_name** | **str** | Database name the agent should use for structured data queries | [optional] 
**table_name** | **str** | Table name the agent should use for structured data queries | [optional] 
**allowed_tools** | **List[str]** | List of tool names the agent is allowed to use | [optional] 
**use_mcp** | **bool** | Whether to enable MCP (Model Context Protocol) integration | [optional] [default to False]
**mcp_server_urls** | **List[str]** | List of MCP server URLs | [optional] 
**agent_strategy** | **str** | Reasoning strategy (&#39;react&#39;, &#39;cot&#39;, etc.) | [optional] [default to 'react']
**stream** | **bool** | Whether to enable streaming responses by default | [optional] [default to False]
**active** | **bool** | Whether the agent is active and available for use | [optional] [default to True]
**agent_origin** | **str** | Origin type: &#39;preset&#39; or &#39;custom&#39; | [optional] [default to 'custom']
**parent_agent_id** | **str** | ID of the parent preset agent if this is a custom agent derived from a preset | [optional] 
**max_trials** | **int** | Maximum number of tool execution cycles | [optional] 

## Example

```python
from verity_ai_pyc.models.agent_create_public import AgentCreatePublic

# TODO update the JSON string below
json = "{}"
# create an instance of AgentCreatePublic from a JSON string
agent_create_public_instance = AgentCreatePublic.from_json(json)
# print the JSON string representation of the object
print(AgentCreatePublic.to_json())

# convert the object into a dict
agent_create_public_dict = agent_create_public_instance.to_dict()
# create an instance of AgentCreatePublic from a dict
agent_create_public_from_dict = AgentCreatePublic.from_dict(agent_create_public_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


