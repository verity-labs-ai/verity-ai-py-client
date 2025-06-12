# 🚀 Verity AI Python Client
Welcome to the most comprehensive and fun way to interact with Verity AI! 🎉

This Python SDK gives you superpowers for:
- 💬 **Chat Completions** - Talk to AI like a pro
- 🤖 **Agent Management** - Create and manage your AI assistants  
- 📁 **File Management** - Upload, list, and delete files with ease
- 🗄️ **RAG Generation** - Both unstructured and structured data magic
- 🔍 **Smart Retrieval** - Find exactly what you need
- ⚡ **Lightning Fast** - Built for speed and simplicity

---

## 📋 What You Need

- 🐍 **Python 3.9+** (the newer, the better!)
- 🔑 **API Key** from Verity AI
- ☕ **Coffee** (optional but recommended)

---

## 🛠️ Installation & Setup

### 🎯 Quick Install

```bash
# The easy way (coming soon to PyPI!)
pip install verity-ai-pyc

# The developer way (for now)
pip install git+https://github.com/your-repo/verity-py-client.git
```

### 🔧 Development Setup

```bash
# Clone and install for development
git clone https://github.com/your-repo/verity-py-client.git
cd verity-py-client
python setup.py install --user
```

### 🔑 Set Your API Key

```bash
# Set your API key (get one from https://chat.veritylabs.ai)
export API_KEY="your-super-secret-api-key-here"
```

---

## 🚀 Getting Started - Let's Have Some Fun!

### 💬 Your First AI Chat

```python
import os
import verity_ai_pyc

# Configure your client
configuration = verity_ai_pyc.Configuration(
    host="https://chat.veritylabs.ai"
)
configuration.api_key['XAPIKeyAuth'] = os.environ["API_KEY"]

# Let's chat! 🎉
with verity_ai_pyc.ApiClient(configuration) as api_client:
    completions_api = verity_ai_pyc.CompletionsApi(api_client)
    
    chat_request = verity_ai_pyc.ChatCompletionRequestPublic(
        model="anthropic_claude_3_5_sonnet_v1",
        messages=[
            verity_ai_pyc.Message(
                role="user", 
                content="Tell me a fun fact about AI! 🤖"
            )
        ],
        data_type="unstructured",
        knowledge_base=verity_ai_pyc.KnowledgeBase("all")
    )
    
    try:
        response = completions_api.create_chat_completion_rag_generation_chat_completions_post(chat_request)
        print("🎉 AI says:", response.messages[0].content)
    except Exception as e:
        print(f"😅 Oops! {e}")
```

### 🗄️ SQL Queries Made Easy

```python
# Ask questions about your database!
chat_request = verity_ai_pyc.ChatCompletionRequestPublic(
    model="anthropic_claude_3_5_sonnet_v1",
    messages=[
        verity_ai_pyc.Message(
            role="user",
            content="How many awesome records do we have? 📊"
        )
    ],
    data_type="structured",
    database_name="your_cool_database"
)
```

### 🤖 Chat with Your Custom Agents

```python
# Use your pre-built agents
chat_request = verity_ai_pyc.ChatCompletionRequestPublic(
    model="anthropic_claude_3_5_sonnet_v1",
    messages=[verity_ai_pyc.Message(role="user", content="Hello, agent! 👋")],
    agent_flag=True,  # 🎯 Agent mode activated!
    agent_id="your_agent_id_here",
    data_type="unstructured",
    knowledge_base=verity_ai_pyc.KnowledgeBase("all")
)
```

### 📁 File Management Fun

```python
# Upload a file (it's that simple!)
file_management_api = verity_ai_pyc.FileManagementApi(api_client)

# Upload some content
response = file_management_api.upload_file_fileman_data_upload_post(
    file=("my_awesome_doc.txt", b"This is amazing content! 🎉"),
    storage_type="unstructured",
    knowledge_base="my_knowledge_base"
)

# List your files
files = file_management_api.list_files_get_fileman_data_list_get(
    storage_type="unstructured",
    page=1,
    page_size=10
)
print(f"📚 You have {len(files.files)} files!")
```

---

## 🎮 Fun Examples & Tutorials

Want to see more? Check out our `examples/` folder for:

- 💬 **Simple Chat Examples** - Basic conversations with AI
- 🤖 **Agent Interactions** - Working with custom agents  
- 📊 **SQL Query Examples** - Database magic made simple
- 📁 **File Upload/Download** - Managing your documents
- 🔍 **Document Search** - Finding needles in haystacks
- 🚀 **Advanced Workflows** - Combining multiple features

```bash
# Run the fun examples!
cd examples/
python example.py
```

---

## 📖 API Documentation

### 🎯 Main Endpoints

| What You Want To Do | API Class | Method | Description |
|---------------------|-----------|--------|-------------|
| 💬 Chat with AI | `CompletionsApi` | `create_chat_completion_*` | Have conversations! |
| 🤖 Manage Agents | `AgentsApi` | `create_agent_*`, `list_agents_*` | Your AI assistant army |
| 📁 Handle Files | `FileManagementApi` | `upload_file_*`, `list_files_*` | File management magic |
| 🔍 Search Docs | `UnstructuredApi` | `retrieve`, `list_kb_documents` | Find anything instantly |
| 🗄️ Query Data | `StructuredApi` | `list_db_tables_*` | Database exploration |
| 🎛️ Check Models | `ModelsApi` | `list_models_*` | See what's available |

### 🏗️ Core Models You'll Love

- 💬 **ChatCompletionRequestPublic** - Your chat configuration
- 🤖 **AgentCreatePublic** - Build new agents
- 📁 **FileInfo** - File details and metadata
- 🔍 **RetrievalRequestPublic** - Search configurations
- 📊 **Message** - Individual chat messages

---

## 🔐 Authentication

Super simple API key authentication:

```python
# Just add your key to the configuration
configuration.api_key['XAPIKeyAuth'] = "your-api-key-here"

# Or use environment variable (recommended!)
configuration.api_key['XAPIKeyAuth'] = os.environ["API_KEY"]
```

The API key goes in the `x-api-key` header - we handle all the details! ✨

---

## 🧪 Testing

```bash
# Run the test suite
pytest

# Run with coverage (for the completionists!)
pytest --cov=verity_ai_pyc
```

---

## 🆘 Need Help?

- 📚 **Documentation**: Check the `docs/` folder for detailed API docs
- 🎯 **Examples**: Look at `examples/example.py` for practical usage
- 🐛 **Issues**: Found a bug? Let us know!
- 💡 **Ideas**: Have suggestions? We'd love to hear them!

---

## 🎉 What's Next?

This SDK is your gateway to building amazing AI-powered applications! Whether you're:

- 🏗️ **Building chatbots** that actually understand context
- 📊 **Creating data analysis tools** that speak human
- 🤖 **Developing AI agents** for specific tasks
- 🔍 **Building search systems** that find exactly what users need

You're in the right place! Welcome to the future of AI development! 🚀

---

*Made with ❤️ by the Verity AI team*


- API version: 1.0.0
- Package version: 0.1.0
- Generator version: 7.13.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.9+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import verity_ai_pyc
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import verity_ai_pyc
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    agent_create_public = verity_ai_pyc.AgentCreatePublic() # AgentCreatePublic | 

    try:
        # Create a new agent
        api_response = api_instance.create_agent_endpoint_v1_agents_post(agent_create_public)
        print("The response of AgentsApi->create_agent_endpoint_v1_agents_post:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentsApi->create_agent_endpoint_v1_agents_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://chat.veritylabs.ai*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AgentsApi* | [**create_agent_endpoint_v1_agents_post**](docs/AgentsApi.md#create_agent_endpoint_v1_agents_post) | **POST** /services/v1/agents/ | Create a new agent
*AgentsApi* | [**delete_agent_endpoint_v1_agents_agent_id_delete**](docs/AgentsApi.md#delete_agent_endpoint_v1_agents_agent_id_delete) | **DELETE** /services/v1/agents/{agent_id} | Archive (soft-delete) an agent
*AgentsApi* | [**get_agent_endpoint_v1_agents_agent_id_get**](docs/AgentsApi.md#get_agent_endpoint_v1_agents_agent_id_get) | **GET** /services/v1/agents/{agent_id} | Get agent by ID
*AgentsApi* | [**list_agents_endpoint_v1_agents_get**](docs/AgentsApi.md#list_agents_endpoint_v1_agents_get) | **GET** /services/v1/agents/ | List all active agents
*AgentsApi* | [**update_agent_endpoint_v1_agents_agent_id_put**](docs/AgentsApi.md#update_agent_endpoint_v1_agents_agent_id_put) | **PUT** /services/v1/agents/{agent_id} | Update an existing agent
*CompletionsApi* | [**create_chat_completion_rag_generation_chat_completions_post**](docs/CompletionsApi.md#create_chat_completion_rag_generation_chat_completions_post) | **POST** /services/rag-generation/chat/completions | chat completions
*FileManagementApi* | [**delete_files_fileman_data_delete_delete**](docs/FileManagementApi.md#delete_files_fileman_data_delete_delete) | **DELETE** /services/fileman/data/delete | delete files
*FileManagementApi* | [**list_files_get_fileman_data_list_get**](docs/FileManagementApi.md#list_files_get_fileman_data_list_get) | **GET** /services/fileman/data/list | list files (GET method)
*FileManagementApi* | [**upload_file_fileman_data_upload_post**](docs/FileManagementApi.md#upload_file_fileman_data_upload_post) | **POST** /services/fileman/data/upload | upload files
*ModelsApi* | [**list_models_rag_generation_models_get**](docs/ModelsApi.md#list_models_rag_generation_models_get) | **GET** /services/rag-generation/models | List Models
*StructuredApi* | [**list_db_tables_unstructured**](docs/StructuredApi.md#list_db_tables_unstructured) | **GET** /services/rag-generation/db_tables | list db tables
*UnstructuredApi* | [**list_kb_documents**](docs/UnstructuredApi.md#list_kb_documents) | **GET** /services/rag-generation/kb_docs | list knowledge base documents
*UnstructuredApi* | [**retrieve**](docs/UnstructuredApi.md#retrieve) | **POST** /services/rag-generation/retrieve | retrieve unstructured data
*UnstructuredApi* | [**validate_ingestion_rag_generation_validate_ingestion_post**](docs/UnstructuredApi.md#validate_ingestion_rag_generation_validate_ingestion_post) | **POST** /services/rag-generation/validate_ingestion | Validate ingestion status of uploaded documents


## Documentation For Models

 - [AgentCreatePublic](docs/AgentCreatePublic.md)
 - [AgentResponse](docs/AgentResponse.md)
 - [AgentUpdatePublic](docs/AgentUpdatePublic.md)
 - [ChatCompletionMessage](docs/ChatCompletionMessage.md)
 - [ChatCompletionRequestPublic](docs/ChatCompletionRequestPublic.md)
 - [ChatCompletionResponse](docs/ChatCompletionResponse.md)
 - [CrawlerJobRequestPublic](docs/CrawlerJobRequestPublic.md)
 - [CrawlerJobResponse](docs/CrawlerJobResponse.md)
 - [CrawlerJobStatusResponse](docs/CrawlerJobStatusResponse.md)
 - [CreateSessionPayload](docs/CreateSessionPayload.md)
 - [DeleteRequest](docs/DeleteRequest.md)
 - [DeleteResponse](docs/DeleteResponse.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [FileInfo](docs/FileInfo.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [KnowledgeBase](docs/KnowledgeBase.md)
 - [KnowledgeBase1](docs/KnowledgeBase1.md)
 - [KnowledgeBase2](docs/KnowledgeBase2.md)
 - [ListFilesPagination](docs/ListFilesPagination.md)
 - [ListFilesResponse](docs/ListFilesResponse.md)
 - [Message](docs/Message.md)
 - [NextToken](docs/NextToken.md)
 - [RetrievalRequestPublic](docs/RetrievalRequestPublic.md)
 - [UploadFileResponse](docs/UploadFileResponse.md)
 - [Usage](docs/Usage.md)
 - [UserDetailsRequest](docs/UserDetailsRequest.md)
 - [ValidateDocsRequest](docs/ValidateDocsRequest.md)
 - [ValidateDocsResponse](docs/ValidateDocsResponse.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorLocInner](docs/ValidationErrorLocInner.md)


