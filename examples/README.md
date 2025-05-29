# Verity AI Python SDK Examples

This directory contains examples demonstrating how to use the Verity AI Python SDK with x-api-key authentication.

## Files

- **`example.py`** - Simple, easy-to-use examples covering all API endpoints
- **`workaround_example.py`** - Alternative implementation with manual patching (for reference)
- **`README.md`** - This file

## Prerequisites

1. **Install the SDK**:
   ```bash
   cd sdk/python
   pip install -e .
   ```

2. **Set your API key**:
   ```bash
   export API_KEY="your-api-key-here"
   ```
   
   Or create a `.env` file in the parent directory:
   ```
   API_KEY=your-api-key-here
   ```

## Quick Start

### Simple Usage (Recommended)

```python
from example import VerityAIExamples

# Initialize the client
client = VerityAIExamples()

# List available models
models = client.list_models()

# Ask questions about documents
response = client.chat("What is COVID-19?")

# Query databases with natural language
sql_response = client.sql_chat("How many patients are in the database?")

# Use AI agents for complex reasoning
agent_response = client.agent_chat("Analyze the relationship between age and outcomes")

# Search documents
docs = client.search_documents("machine learning", top_k=5)

# List resources
files = client.list_files("unstructured")
databases = client.list_databases()
knowledge_bases = client.list_knowledge_bases()
```

### Run All Examples

```bash
cd sdk/examples
python example.py
```

## API Methods

### Chat & Completion

- **`client.chat(query, knowledge_base="all", model=None)`** - Chat with documents
- **`client.sql_chat(query, database="veritydemo_mimic", model=None)`** - Natural language SQL queries
- **`client.agent_chat(query, data_type="unstructured", model=None)`** - AI agent with reasoning

### Search & Retrieval

- **`client.search_documents(query, knowledge_base="all", top_k=5)`** - Semantic document search
- **`client.list_models()`** - List available LLM models

### Resource Management

- **`client.list_files(storage_type="unstructured", limit=10)`** - List files
- **`client.list_databases()`** - List databases and tables
- **`client.list_knowledge_bases()`** - List knowledge bases and documents

### File Operations

- **`client.upload_file(file_path, storage_type, knowledge_base=None)`** - Upload files
- **`client.delete_files(filenames, storage_type)`** - Delete files

## Examples by Use Case

### Document Q&A
```python
client = VerityAIExamples()

# Ask about your documents
response = client.chat("What are the key findings in the research papers?")
print(response)

# Search for specific information
docs = client.search_documents("COVID-19 symptoms", top_k=3)
for doc in docs:
    print(f"Source: {doc.get('source', 'Unknown')}")
    print(f"Text: {doc.get('text', '')[:200]}...")
```

### Database Analysis
```python
client = VerityAIExamples()

# Natural language database queries
response = client.sql_chat("What is the average age of patients?")
print(response)

# Complex analysis with AI agent
analysis = client.agent_chat(
    "Compare patient outcomes by age group and identify trends",
    data_type="structured"
)
print(analysis)
```

### File Management
```python
client = VerityAIExamples()

# List your files
files = client.list_files("unstructured")
for file in files[:5]:
    print(f"{file.filename} ({file.size_mb:.2f} MB)")

# Upload a new document
client.upload_file(
    "my_document.pdf", 
    "unstructured", 
    knowledge_base="my_knowledge_base"
)
```

## Error Handling

The SDK includes automatic error handling and informative error messages:

```python
try:
    response = client.chat("Your question here")
    print(response)
except Exception as e:
    print(f"Error: {e}")
```

## Advanced Usage

For more detailed control over requests, you can access the underlying API objects:

```python
client = VerityAIExamples()

# Access raw API clients
models_api = client.models_api
completions_api = client.completions_api
unstructured_api = client.unstructured_api
structured_api = client.structured_api
file_management_api = client.file_management_api
```

## Troubleshooting

### API Key Issues
- Make sure your API key is set: `export API_KEY="your-key"`
- Check that the key is valid and has the right permissions

### Import Errors
- Install the SDK: `cd sdk/python && pip install -e .`
- Make sure you're in the right Python environment

### Model Availability
- Different models are available based on your tier
- Use `client.list_models()` to see what's available to you

## Support

For more information, see the main SDK documentation or contact Verity AI support. 