# Verity AI Python Client

[![PyPI version](https://badge.fury.io/py/verity-ai-client.svg)](https://badge.fury.io/py/verity-ai-client)
[![Python Support](https://img.shields.io/pypi/pyversions/verity-ai-client.svg)](https://pypi.org/project/verity-ai-client/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Official Python client for **Verity AI** - A comprehensive API service for unstructured and structured RAG (Retrieval-Augmented Generation), file management, AI interactions, and knowledge base operations.

## 🚀 Features

- **RAG Generation**: Powerful retrieval-augmented generation for both structured and unstructured data
- **File Management**: Upload, list, and delete files with ease
- **Knowledge Base Operations**: Manage and query knowledge bases
- **Database Integration**: Natural language SQL queries and database operations
- **AI Chat Completions**: Advanced chat completions with multiple AI models
- **Type Safety**: Full type hints and Pydantic models for better development experience

## Requirements

Python 3.9+

## Installation & Usage

### PyPI Installation (Recommended)

Install the Verity AI Python client using pip:

```bash
pip install verity-ai-client
```

For development with optional dependencies:

```bash
pip install verity-ai-client[dev]
```

### Alternative Installation Methods

#### Install from GitHub Repository

If you need the latest development version:

```sh
pip install git+https://github.com/verity-labs-ai/verity-ai-py-client.git
```

#### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools):

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

### Import the Package

```python
import verity_ai_pyc
```

## 🔧 Quick Start

### Authentication

First, obtain your API key from [Verity Labs](https://veritylabs.ai/auth) go to settings, create API Key and set it as an environment variable:

```bash
export VERITY_API_KEY="your-api-key-here"
```

### Basic Configuration

```python
import os
import verity_ai_pyc
from verity_ai_pyc.rest import ApiException

# Configure the client
configuration = verity_ai_pyc.Configuration(
    host="https://chat.veritylabs.ai"
)
configuration.api_key['XAPIKeyAuth'] = os.environ["VERITY_API_KEY"]

# Create API client
api_client = verity_ai_pyc.ApiClient(configuration)
```

## 📚 Examples

### 1. List Available Models

```python
import os
import verity_ai_pyc
from verity_ai_pyc.rest import ApiException

# Configure the client
configuration = verity_ai_pyc.Configuration(host="https://chat.veritylabs.ai")
configuration.api_key['XAPIKeyAuth'] = os.environ["VERITY_API_KEY"]

with verity_ai_pyc.ApiClient(configuration) as api_client:
    models_api = verity_ai_pyc.ModelsApi(api_client)
    try:
        models = models_api.list_models_rag_generation_models_get()
        print("Available models:")
        for model in models.data:
            print(f"- {model.id}")
    except ApiException as e:
        print(f"Error listing models: {e}")
```

### 2. Chat Completions

```python
import os
import verity_ai_pyc
from verity_ai_pyc.rest import ApiException

configuration = verity_ai_pyc.Configuration(host="https://chat.veritylabs.ai")
configuration.api_key['XAPIKeyAuth'] = os.environ["VERITY_API_KEY"]

with verity_ai_pyc.ApiClient(configuration) as api_client:
    completions_api = verity_ai_pyc.CompletionsApi(api_client)
    
    # Create a chat completion request
    chat_request = verity_ai_pyc.ChatCompletionRequestPublic(
        model="anthropic_claude_3_5_sonnet_v1",
        messages=[
            verity_ai_pyc.ChatCompletionMessage(
                role="user",
                content="What is artificial intelligence?"
            )
        ],
        max_tokens=150
    )
    
    try:
        response = completions_api.create_chat_completion_rag_generation_chat_completions_post(chat_request)
        print("AI Response:", response.choices[0].message.content)
    except ApiException as e:
        print(f"Chat completion error: {e}")
```

### 3. File Management

#### Upload a File

```python
import os
import verity_ai_pyc
from verity_ai_pyc.rest import ApiException

configuration = verity_ai_pyc.Configuration(host="https://chat.veritylabs.ai")
configuration.api_key['XAPIKeyAuth'] = os.environ["VERITY_API_KEY"]

with verity_ai_pyc.ApiClient(configuration) as api_client:
    file_api = verity_ai_pyc.FileManagementApi(api_client)
    
    # Upload a file
    with open("document.pdf", "rb") as file:
        try:
            upload_response = file_api.upload_file_fileman_data_upload_post(
                file=file,
                knowledge_base_id="your-kb-id"
            )
            print(f"File uploaded successfully: {upload_response.file_id}")
        except ApiException as e:
            print(f"Upload error: {e}")
```

#### List Files

```python
import os
import verity_ai_pyc
from verity_ai_pyc.rest import ApiException

configuration = verity_ai_pyc.Configuration(host="https://chat.veritylabs.ai")
configuration.api_key['XAPIKeyAuth'] = os.environ["VERITY_API_KEY"]

with verity_ai_pyc.ApiClient(configuration) as api_client:
    file_api = verity_ai_pyc.FileManagementApi(api_client)
    
    try:
        files = file_api.list_files_get_fileman_data_list_get()
        print("Your files:")
        for file in files.files:
            print(f"- {file.filename} (ID: {file.file_id})")
    except ApiException as e:
        print(f"List files error: {e}")
```

#### Delete Files

```python
import os
import verity_ai_pyc
from verity_ai_pyc.rest import ApiException

configuration = verity_ai_pyc.Configuration(host="https://chat.veritylabs.ai")
configuration.api_key['XAPIKeyAuth'] = os.environ["VERITY_API_KEY"]

with verity_ai_pyc.ApiClient(configuration) as api_client:
    file_api = verity_ai_pyc.FileManagementApi(api_client)
    
    delete_request = verity_ai_pyc.DeleteRequest(
        file_ids=["file-id-1", "file-id-2"]
    )
    
    try:
        response = file_api.delete_files_fileman_data_delete_delete(delete_request)
        print(f"Deleted {len(response.deleted_files)} files")
    except ApiException as e:
        print(f"Delete error: {e}")
```

### 4. Knowledge Base Retrieval

```python
import os
import verity_ai_pyc
from verity_ai_pyc.rest import ApiException

configuration = verity_ai_pyc.Configuration(host="https://chat.veritylabs.ai")
configuration.api_key['XAPIKeyAuth'] = os.environ["VERITY_API_KEY"]

with verity_ai_pyc.ApiClient(configuration) as api_client:
    unstructured_api = verity_ai_pyc.UnstructuredApi(api_client)
    
    # Retrieve relevant documents
    retrieval_request = verity_ai_pyc.RetrievalRequestPublic(
        query="machine learning algorithms",
        top_k=5,
        knowledge_base_id="your-kb-id"
    )
    
    try:
        results = unstructured_api.retrieve(retrieval_request)
        print(f"Retrieved {len(results.documents)} documents:")
        for i, doc in enumerate(results.documents, 1):
            print(f"{i}. {doc.content[:100]}...")
    except ApiException as e:
        print(f"Retrieval error: {e}")
```

### 5. List Knowledge Base Documents

```python
import os
import verity_ai_pyc
from verity_ai_pyc.rest import ApiException

configuration = verity_ai_pyc.Configuration(host="https://chat.veritylabs.ai")
configuration.api_key['XAPIKeyAuth'] = os.environ["VERITY_API_KEY"]

with verity_ai_pyc.ApiClient(configuration) as api_client:
    unstructured_api = verity_ai_pyc.UnstructuredApi(api_client)
    
    try:
        kb_docs = unstructured_api.list_kb_documents()
        print("Knowledge base documents:")
        for doc in kb_docs:
            print(f"- {doc}")
    except ApiException as e:
        print(f"Error listing KB documents: {e}")
```

### 6. Validate Document Ingestion

```python
import os
import verity_ai_pyc
from verity_ai_pyc.rest import ApiException

configuration = verity_ai_pyc.Configuration(host="https://chat.veritylabs.ai")
configuration.api_key['XAPIKeyAuth'] = os.environ["VERITY_API_KEY"]

with verity_ai_pyc.ApiClient(configuration) as api_client:
    unstructured_api = verity_ai_pyc.UnstructuredApi(api_client)
    
    validate_request = verity_ai_pyc.ValidateDocsRequest(
        file_ids=["file-id-1", "file-id-2"]
    )
    
    try:
        validation = unstructured_api.validate_ingestion_rag_generation_validate_ingestion_post(validate_request)
        print("Validation results:")
        print(f"Status: {validation.status}")
        print(f"Message: {validation.message}")
    except ApiException as e:
        print(f"Validation error: {e}")
```

### Tests

Execute `pytest` to run the tests:

```bash
pytest
```

## Documentation for API Endpoints

All URIs are relative to *https://chat.veritylabs.ai*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CompletionsApi* | [**create_chat_completion_rag_generation_chat_completions_post**](docs/CompletionsApi.md#create_chat_completion_rag_generation_chat_completions_post) | **POST** /services/rag-generation/chat/completions | chat completions
*FileManagementApi* | [**delete_files_fileman_data_delete_delete**](docs/FileManagementApi.md#delete_files_fileman_data_delete_delete) | **DELETE** /services/fileman/data/delete | delete files
*FileManagementApi* | [**list_files_get_fileman_data_list_get**](docs/FileManagementApi.md#list_files_get_fileman_data_list_get) | **GET** /services/fileman/data/list | list files (GET method)
*FileManagementApi* | [**upload_file_fileman_data_upload_post**](docs/FileManagementApi.md#upload_file_fileman_data_upload_post) | **POST** /services/fileman/data/upload | upload files
*ModelsApi* | [**list_models_rag_generation_models_get**](docs/ModelsApi.md#list_models_rag_generation_models_get) | **GET** /services/rag-generation/models | List Models
*StructuredApi* | [**list_db_tables_unstructured**](docs/StructuredApi.md#list_db_tables_unstructured) | **GET** /services/rag-generation/db_tables | list db tables
*UnstructuredApi* | [**list_kb_documents**](docs/UnstructuredApi.md#list_kb_documents) | **GET** /services/rag-generation/kb_docs | list knowledge base documents
*UnstructuredApi* | [**retrieve**](docs/UnstructuredApi.md#retrieve) | **POST** /services/rag-generation/retrieve | retrieve unstructured data
*UnstructuredApi* | [**validate_ingestion_rag_generation_validate_ingestion_post**](docs/UnstructuredApi.md#validate_ingestion_rag_generation_validate_ingestion_post) | **POST** /services/rag-generation/validate_ingestion | Validate ingestion status of uploaded documents

### Available APIs

- **CompletionsApi**: Chat completions and AI interactions
- **FileManagementApi**: File upload, listing, and deletion
- **ModelsApi**: List available AI models
- **UnstructuredApi**: Knowledge base and document operations
- **StructuredApi**: Database and SQL operations

## Documentation For Models

 - [AgentCreatePublic](docs/AgentCreatePublic.md)
 - [AgentResponse](docs/AgentResponse.md)
 - [AgentUpdatePublic](docs/AgentUpdatePublic.md)
 - [ChatCompletionMessage](docs/ChatCompletionMessage.md)
 - [ChatCompletionRequestPublic](docs/ChatCompletionRequestPublic.md)
 - [ChatCompletionResponse](docs/ChatCompletionResponse.md)
 - [DeleteRequest](docs/DeleteRequest.md)
 - [DeleteResponse](docs/DeleteResponse.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [FileInfo](docs/FileInfo.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [KnowledgeBase](docs/KnowledgeBase.md)
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

### Key Models

- `ChatCompletionRequestPublic`: Request structure for chat completions
- `ChatCompletionResponse`: Response from chat completions
- `FileInfo`: File metadata and information
- `RetrievalRequestPublic`: Document retrieval requests
- `ValidateDocsRequest`: Document validation requests

## 🔒 Authentication

The Verity AI API uses API key authentication. Include your API key in the `x-api-key` header:

```python
configuration.api_key['XAPIKeyAuth'] = "your-api-key"
```

<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Authentication schemes defined for the API:
<a id="XAPIKeyAuth"></a>
### XAPIKeyAuth

- **Type**: API key
- **API key parameter name**: x-api-key
- **Location**: HTTP header

## 📄 License

This project is licensed under the MIT License.

## 🤝 Contributing

We welcome contributions! Please see our Contributing Guidelines for details.

## 📞 Support

- **Documentation**: [https://docs.veritylabs.ai](https://docs.veritylabs.ai)
- **Issues**: [GitHub Issues](https://github.com/veritylabs/verity-ai-python-client/issues)
- **Email**: support@veritylabs.ai

## 🔗 Links

- **Homepage**: [https://veritylabs.ai](https://veritylabs.ai)
- **PyPI**: [https://pypi.org/project/verity-ai-client/](https://pypi.org/project/verity-ai-client/)
- **GitHub**: [https://github.com/veritylabs/verity-ai-python-client](https://github.com/veritylabs/verity-ai-python-client)

---

Built with ❤️ by [Verity Labs](https://veritylabs.ai)




