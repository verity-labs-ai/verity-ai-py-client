# verity_ai_pyc.AgentsApi

All URIs are relative to *https://chat.veritylabs.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_agent_endpoint_v1_agents_post**](AgentsApi.md#create_agent_endpoint_v1_agents_post) | **POST** /services/v1/agents/ | Create a new agent
[**delete_agent_endpoint_v1_agents_agent_id_delete**](AgentsApi.md#delete_agent_endpoint_v1_agents_agent_id_delete) | **DELETE** /services/v1/agents/{agent_id} | Archive (soft-delete) an agent
[**get_agent_endpoint_v1_agents_agent_id_get**](AgentsApi.md#get_agent_endpoint_v1_agents_agent_id_get) | **GET** /services/v1/agents/{agent_id} | Get agent by ID
[**list_agents_endpoint_v1_agents_get**](AgentsApi.md#list_agents_endpoint_v1_agents_get) | **GET** /services/v1/agents/ | List all active agents
[**update_agent_endpoint_v1_agents_agent_id_put**](AgentsApi.md#update_agent_endpoint_v1_agents_agent_id_put) | **PUT** /services/v1/agents/{agent_id} | Update an existing agent


# **create_agent_endpoint_v1_agents_post**
> AgentResponse create_agent_endpoint_v1_agents_post(agent_create_public)

Create a new agent

Create a new agent with specified metadata under the current organization. For custom agents, ensure parent_agent_id is provided.

### Example

* Api Key Authentication (XAPIKeyAuth):

```python
import verity_ai_pyc
from verity_ai_pyc.models.agent_create_public import AgentCreatePublic
from verity_ai_pyc.models.agent_response import AgentResponse
from verity_ai_pyc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://chat.veritylabs.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = verity_ai_pyc.Configuration(
    host = "https://chat.veritylabs.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: XAPIKeyAuth
configuration.api_key['XAPIKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XAPIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with verity_ai_pyc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = verity_ai_pyc.AgentsApi(api_client)
    agent_create_public = verity_ai_pyc.AgentCreatePublic() # AgentCreatePublic | 

    try:
        # Create a new agent
        api_response = api_instance.create_agent_endpoint_v1_agents_post(agent_create_public)
        print("The response of AgentsApi->create_agent_endpoint_v1_agents_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->create_agent_endpoint_v1_agents_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_create_public** | [**AgentCreatePublic**](AgentCreatePublic.md)|  | 

### Return type

[**AgentResponse**](AgentResponse.md)

### Authorization

[XAPIKeyAuth](../README.md#XAPIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_agent_endpoint_v1_agents_agent_id_delete**
> delete_agent_endpoint_v1_agents_agent_id_delete(agent_id)

Archive (soft-delete) an agent

Soft-delete an agent by setting active=false. Preserves audit trail by not hard-deleting.

### Example

* Api Key Authentication (XAPIKeyAuth):

```python
import verity_ai_pyc
from verity_ai_pyc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://chat.veritylabs.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = verity_ai_pyc.Configuration(
    host = "https://chat.veritylabs.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: XAPIKeyAuth
configuration.api_key['XAPIKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XAPIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with verity_ai_pyc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = verity_ai_pyc.AgentsApi(api_client)
    agent_id = 'agent_id_example' # str | 

    try:
        # Archive (soft-delete) an agent
        api_instance.delete_agent_endpoint_v1_agents_agent_id_delete(agent_id)
    except Exception as e:
        print("Exception when calling AgentsApi->delete_agent_endpoint_v1_agents_agent_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[XAPIKeyAuth](../README.md#XAPIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_endpoint_v1_agents_agent_id_get**
> AgentResponse get_agent_endpoint_v1_agents_agent_id_get(agent_id)

Get agent by ID

Retrieve the full definition of an agent by its ID if it belongs to the current organization.

### Example

* Api Key Authentication (XAPIKeyAuth):

```python
import verity_ai_pyc
from verity_ai_pyc.models.agent_response import AgentResponse
from verity_ai_pyc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://chat.veritylabs.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = verity_ai_pyc.Configuration(
    host = "https://chat.veritylabs.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: XAPIKeyAuth
configuration.api_key['XAPIKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XAPIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with verity_ai_pyc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = verity_ai_pyc.AgentsApi(api_client)
    agent_id = 'agent_id_example' # str | 

    try:
        # Get agent by ID
        api_response = api_instance.get_agent_endpoint_v1_agents_agent_id_get(agent_id)
        print("The response of AgentsApi->get_agent_endpoint_v1_agents_agent_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_agent_endpoint_v1_agents_agent_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 

### Return type

[**AgentResponse**](AgentResponse.md)

### Authorization

[XAPIKeyAuth](../README.md#XAPIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_agents_endpoint_v1_agents_get**
> List[AgentResponse] list_agents_endpoint_v1_agents_get(origin_type=origin_type, active=active, limit=limit)

List all active agents

Retrieve all active agents for the current organization. Supports optional filters such as origin_type.

### Example

* Api Key Authentication (XAPIKeyAuth):

```python
import verity_ai_pyc
from verity_ai_pyc.models.agent_response import AgentResponse
from verity_ai_pyc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://chat.veritylabs.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = verity_ai_pyc.Configuration(
    host = "https://chat.veritylabs.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: XAPIKeyAuth
configuration.api_key['XAPIKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XAPIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with verity_ai_pyc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = verity_ai_pyc.AgentsApi(api_client)
    origin_type = 'origin_type_example' # str | Filter by origin type: 'preset' or 'custom' (optional)
    active = True # bool | Filter by active status (optional) (default to True)
    limit = 56 # int | Maximum number of agents to return (optional)

    try:
        # List all active agents
        api_response = api_instance.list_agents_endpoint_v1_agents_get(origin_type=origin_type, active=active, limit=limit)
        print("The response of AgentsApi->list_agents_endpoint_v1_agents_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->list_agents_endpoint_v1_agents_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin_type** | **str**| Filter by origin type: &#39;preset&#39; or &#39;custom&#39; | [optional] 
 **active** | **bool**| Filter by active status | [optional] [default to True]
 **limit** | **int**| Maximum number of agents to return | [optional] 

### Return type

[**List[AgentResponse]**](AgentResponse.md)

### Authorization

[XAPIKeyAuth](../README.md#XAPIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agent_endpoint_v1_agents_agent_id_put**
> AgentResponse update_agent_endpoint_v1_agents_agent_id_put(agent_id, agent_update_public)

Update an existing agent

Update one or more fields of an existing agent belonging to the current organization.

### Example

* Api Key Authentication (XAPIKeyAuth):

```python
import verity_ai_pyc
from verity_ai_pyc.models.agent_response import AgentResponse
from verity_ai_pyc.models.agent_update_public import AgentUpdatePublic
from verity_ai_pyc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://chat.veritylabs.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = verity_ai_pyc.Configuration(
    host = "https://chat.veritylabs.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: XAPIKeyAuth
configuration.api_key['XAPIKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XAPIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with verity_ai_pyc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = verity_ai_pyc.AgentsApi(api_client)
    agent_id = 'agent_id_example' # str | 
    agent_update_public = verity_ai_pyc.AgentUpdatePublic() # AgentUpdatePublic | 

    try:
        # Update an existing agent
        api_response = api_instance.update_agent_endpoint_v1_agents_agent_id_put(agent_id, agent_update_public)
        print("The response of AgentsApi->update_agent_endpoint_v1_agents_agent_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->update_agent_endpoint_v1_agents_agent_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **agent_update_public** | [**AgentUpdatePublic**](AgentUpdatePublic.md)|  | 

### Return type

[**AgentResponse**](AgentResponse.md)

### Authorization

[XAPIKeyAuth](../README.md#XAPIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

