#!/usr/bin/env python3
"""
Verity AI Python SDK Examples

This file demonstrates how to use each endpoint available in the Verity AI API
using the Python SDK with x-api-key authentication.

Prerequisites:
1. Install the SDK: pip install -e .
2. Set your API key as an environment variable: export API_KEY="your-api-key-here"
3. Ensure you have the required test files in the appropriate directories

Author: Verity AI Labs
"""

import os
import json
import time
from pathlib import Path
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv
load_dotenv("../.env")

try:
    import verity_ai_pyc
    from verity_ai_pyc.rest import ApiException
    from verity_ai_pyc.models import (
        ChatCompletionRequestPublic,
        Message,
        RetrievalRequestPublic,
        ValidateDocsRequest,
        DeleteRequest
    )
except ImportError as e:
    print(f"❌ Error importing Verity AI SDK: {e}")
    print("💡 Make sure to install the SDK first:")
    print("   cd sdk/python && pip install -e .")
    raise


class VerityAIExamples:
    """
    A comprehensive example class demonstrating all Verity AI API endpoints
    using the Python SDK with x-api-key authentication.
    
    Simple usage:
        client = VerityAIExamples()
        models = client.list_models()
        response = client.chat("What is COVID-19?")
    """
    
    def __init__(self, api_key: Optional[str] = None, base_url: str = "https://chat.veritylabs.ai"):
        """
        Initialize the Verity AI client with API key authentication.
        
        Args:
            api_key: Your Verity AI API key. If None, will try to get from API_KEY env var
            base_url: The base URL for the API (default: production URL)
        """
        # Get API key from parameter or environment variable
        self.api_key = api_key or os.getenv("API_KEY")
        if not self.api_key:
            raise ValueError("API key is required. Set API_KEY environment variable or pass api_key parameter.")
        
        # Configure the SDK
        self.configuration = verity_ai_pyc.Configuration(host=base_url)
        self.configuration.api_key['XAPIKeyAuth'] = self.api_key
        
        # Initialize API client
        self.api_client = verity_ai_pyc.ApiClient(self.configuration)
        
        # Initialize API instances
        self.models_api = verity_ai_pyc.ModelsApi(self.api_client)
        self.completions_api = verity_ai_pyc.CompletionsApi(self.api_client)
        self.unstructured_api = verity_ai_pyc.UnstructuredApi(self.api_client)
        self.structured_api = verity_ai_pyc.StructuredApi(self.api_client)
        self.file_management_api = verity_ai_pyc.FileManagementApi(self.api_client)
        
        print(f"✅ Verity AI SDK initialized with base URL: {base_url}")

    def list_models(self):
        """
        List available models.
        
        Returns:
            List of available model names
        """
        print("\n🔍 Listing available models...")
        
        try:
            models_response = self.models_api.list_models_rag_generation_models_get()
            
            # Handle different response formats
            if isinstance(models_response, str):
                # If it's a string representation of a JSON array, parse it
                try:
                    import ast
                    models = ast.literal_eval(models_response)
                except:
                    # If that fails, try JSON parsing
                    try:
                        models = json.loads(models_response)
                    except:
                        # If all else fails, treat as a single model
                        models = [models_response]
            elif isinstance(models_response, list):
                models = models_response
            else:
                # Convert to list if it's some other type
                models = [str(models_response)]
            
            print(f"✅ Found {len(models)} available models:")
            for i, model in enumerate(models, 1):
                print(f"   {i}. {model}")
            return models
            
        except ApiException as e:
            print(f"❌ Error listing models: {e}")
            raise

    def chat(self, query: str, knowledge_base: str = "all", model: str = None):
        """
        Simple chat with unstructured data (documents).
        
        Args:
            query: Your question
            knowledge_base: Which knowledge base to search (default: "all")
            model: Model to use (if None, uses first available model)
            
        Returns:
            Assistant's response text
        """
        print(f"\n💬 Chat: {query}")
        
        try:
            # Get model if not specified
            if model is None:
                models = self.list_models()
                model = models[0] if models else "anthropic_claude_3_haiku_v1"
            
            # Create the request
            request = ChatCompletionRequestPublic(
                model=model,
                messages=[Message(role="user", content=query)],
                knowledge_base=knowledge_base,
                data_type="unstructured",
                agent_flag=False,
                stream=False
            )
            
            # Call the API
            response = self.completions_api.create_chat_completion_rag_generation_chat_completions_post(request)
            
            # Extract the response text
            if response.messages and len(response.messages) > 0:
                assistant_response = response.messages[0].content
                print(f"✅ Response: {assistant_response[:200]}...")
                return assistant_response
            else:
                print("❌ No response received")
                return None
                
        except ApiException as e:
            print(f"❌ Error in chat: {e}")
            raise

    def sql_chat(self, query: str, database: str = "veritydemo_mimic", model: str = None):
        """
        Simple chat with structured data (SQL database).
        
        Args:
            query: Your natural language question about the data
            database: Database name to query
            model: Model to use (if None, uses first available model)
            
        Returns:
            Assistant's response text
        """
        print(f"\n🗄️ SQL Chat: {query}")
        
        try:
            # Get model if not specified
            if model is None:
                models = self.list_models()
                model = models[0] if models else "anthropic_claude_3_haiku_v1"
            
            # Create the request
            request = ChatCompletionRequestPublic(
                model=model,
                messages=[Message(role="user", content=query)],
                database_name=database,
                data_type="structured",
                agent_flag=False,
                stream=False
            )
            
            # Call the API
            response = self.completions_api.create_chat_completion_rag_generation_chat_completions_post(request)
            
            # Extract the response text
            if response.messages and len(response.messages) > 0:
                assistant_response = response.messages[0].content
                print(f"✅ Response: {assistant_response[:200]}...")
                return assistant_response
            else:
                print("❌ No response received")
                return None
                
        except ApiException as e:
            print(f"❌ Error in SQL chat: {e}")
            raise

    def agent_chat(self, query: str, data_type: str = "unstructured", model: str = None):
        """
        Chat with AI agent (advanced reasoning and tool usage).
        
        Args:
            query: Complex question for the agent
            data_type: "unstructured" or "structured"
            model: Model to use (agents work best with advanced models)
            
        Returns:
            Agent's response text
        """
        print(f"\n🤖 Agent Chat ({data_type}): {query}")
        
        try:
            # Get model if not specified (prefer advanced models for agents)
            if model is None:
                models = self.list_models()
                # Try to find a Sonnet model for better agent performance
                advanced_models = [m for m in models if "sonnet" in m.lower()]
                model = advanced_models[0] if advanced_models else (models[0] if models else "anthropic_claude_3_5_sonnet_v1")
            
            # Create the request based on data type
            if data_type == "unstructured":
                request = ChatCompletionRequestPublic(
                    model=model,
                    messages=[Message(role="user", content=query)],
                    knowledge_base="all",
                    data_type="unstructured",
                    agent_flag=True,
                    agent_history_enabled=True,
                    agent_strategy="react",
                    stream=False
                )
            else:  # structured
                request = ChatCompletionRequestPublic(
                    model=model,
                    messages=[Message(role="user", content=query)],
                    database_name="veritydemo_mimic",
                    data_type="structured",
                    agent_flag=True,
                    agent_history_enabled=True,
                    agent_strategy="react",
                    stream=False
                )
            
            # Call the API
            response = self.completions_api.create_chat_completion_rag_generation_chat_completions_post(request)
            
            # Extract the response text
            if response.messages and len(response.messages) > 0:
                assistant_response = response.messages[0].content
                print(f"✅ Agent Response: {assistant_response[:200]}...")
                return assistant_response
            else:
                print("❌ No response received")
                return None
                
        except ApiException as e:
            print(f"❌ Error in agent chat: {e}")
            raise

    def search_documents(self, query: str, knowledge_base: str = "all", top_k: int = 5):
        """
        Search for relevant documents.
        
        Args:
            query: Search query
            knowledge_base: Which knowledge base to search
            top_k: Number of documents to return
            
        Returns:
            List of relevant documents
        """
        print(f"\n🔍 Searching documents: {query}")
        
        try:
            request = RetrievalRequestPublic(
                query=query,
                knowledge_base=knowledge_base,
                top_k=top_k
            )
            
            response = self.unstructured_api.retrieve(request)
            
            # Handle different response formats
            if hasattr(response, 'results') and response.results:
                documents = response.results
            elif hasattr(response, 'documents') and response.documents:
                documents = response.documents
            else:
                documents = response if isinstance(response, list) else []
            
            print(f"✅ Found {len(documents)} relevant documents")
            return documents
            
        except ApiException as e:
            print(f"❌ Error searching documents: {e}")
            raise

    def list_files(self, storage_type: str = "unstructured", limit: int = 10):
        """
        List files in storage.
        
        Args:
            storage_type: "unstructured" or "structured"
            limit: Number of files to show
            
        Returns:
            List of files
        """
        print(f"\n📁 Listing {storage_type} files...")
        
        try:
            response = self.file_management_api.list_files_get_fileman_data_list_get(
                storage_type=storage_type,
                page=1,
                page_size=limit
            )
            
            print(f"✅ Found {len(response.files)} files:")
            for i, file_info in enumerate(response.files[:5], 1):
                file_type = "📁 DIR" if file_info.is_directory else "📄 FILE"
                print(f"   {i}. {file_type} {file_info.filename} ({file_info.size_mb:.2f} MB)")
            
            if len(response.files) > 5:
                print(f"   ... and {len(response.files) - 5} more files")
            
            return response.files
            
        except ApiException as e:
            print(f"❌ Error listing files: {e}")
            raise

    def list_databases(self):
        """
        List available databases and tables.
        
        Returns:
            Dictionary of databases and their tables
        """
        print(f"\n🗄️ Listing databases...")
        
        try:
            response = self.structured_api.list_db_tables_unstructured()
            
            print("✅ Databases found:")
            if isinstance(response, dict):
                for db_name, tables in response.items():
                    table_count = len(tables) if isinstance(tables, list) else "N/A"
                    print(f"   🗃️ {db_name}: {table_count} tables")
            
            return response
            
        except ApiException as e:
            print(f"❌ Error listing databases: {e}")
            raise

    def list_knowledge_bases(self):
        """
        List knowledge bases and their documents.
        
        Returns:
            Dictionary of knowledge bases and documents
        """
        print(f"\n📚 Listing knowledge bases...")
        
        try:
            response = self.unstructured_api.list_kb_documents(page=1, page_size=50)
            
            # Handle different response formats
            if hasattr(response, 'documents'):
                documents = response.documents
            else:
                documents = response
            
            print("✅ Knowledge bases found:")
            if isinstance(documents, dict):
                for kb_name, kb_docs in documents.items():
                    print(f"   📁 {kb_name}: {len(kb_docs)} documents")
            
            return documents
            
        except ApiException as e:
            print(f"❌ Error listing knowledge bases: {e}")
            raise

    def upload_file(self, file_path: str, storage_type: str, knowledge_base: str = None, database_name: str = None, table_name: str = None):
        """
        Upload a file to storage.
        
        Args:
            file_path: Path to the file to upload
            storage_type: "structured" or "unstructured"
            knowledge_base: For unstructured files
            database_name: For structured files
            table_name: For structured files
            
        Returns:
            Upload response
        """
        print(f"\n⬆️ Uploading {file_path}...")
        
        if not os.path.exists(file_path):
            print(f"❌ File not found: {file_path}")
            return None
        
        try:
            with open(file_path, 'rb') as file:
                response = self.file_management_api.upload_file_fileman_data_upload_post(
                    file=file,
                    storage_type=storage_type,
                    knowledge_base=knowledge_base,
                    database_name=database_name,
                    table_name=table_name
                )
            
            print(f"✅ File uploaded: {response.s3_path}")
            return response
            
        except ApiException as e:
            print(f"❌ Error uploading file: {e}")
            raise

    def delete_files(self, filenames: List[str], storage_type: str, base_path: str = "", sub_path: str = ""):
        """
        Delete files from storage.
        
        Args:
            filenames: List of filenames to delete
            storage_type: "structured" or "unstructured"
            base_path: Base directory path
            sub_path: Sub-directory path
            
        Returns:
            Delete response
        """
        print(f"\n🗑️ Deleting {len(filenames)} files...")
        
        try:
            delete_request = DeleteRequest(filenames=filenames)
            
            response = self.file_management_api.delete_files_fileman_data_delete_delete(
                storage_type=storage_type,
                base_path=base_path,
                sub_path=sub_path,
                delete_request=delete_request
            )
            
            print(f"✅ Deleted {len(response.deleted_files)} files")
            return response
            
        except ApiException as e:
            print(f"❌ Error deleting files: {e}")
            raise

    def run_examples(self):
        """Run a series of example API calls."""
        print("🚀 Running Verity AI API examples...")
        print("=" * 50)
        
        try:
            # 1. List models
            models = self.list_models()
            
            # 2. Simple chat
            self.chat("What are the main symptoms of COVID-19?")
            
            # 3. SQL chat
            self.sql_chat("How many patients are in the database?")
            
            # 4. Agent chat (if advanced model available)
            if any("sonnet" in model.lower() for model in models):
                self.agent_chat("Analyze patient demographics", "structured")
            
            # 5. Search documents
            self.search_documents("COVID-19 treatment", top_k=5)
            
            # 6. List resources
            self.list_files("unstructured", limit=5)
            self.list_databases()
            self.list_knowledge_bases()
            
            print("\n" + "=" * 50)
            print("✅ All examples completed successfully!")
            
        except Exception as e:
            print(f"\n❌ Example failed: {e}")
            raise


def main():
    """
    Main function demonstrating simple usage.
    """
    try:
        # Initialize the client
        client = VerityAIExamples()
        
        # Simple usage examples
        print("\n🎯 Simple Usage Examples:")
        print("-" * 30)
        
        # List available models
        models = client.list_models()
        
        # Ask a simple question
        response = client.chat("What is artificial intelligence?")
        
        # Query a database
        sql_response = client.sql_chat("How many records are in the database?")
        
        # Search documents
        docs = client.search_documents("machine learning", top_k=5)
        
        print("\n🎉 Simple examples completed!")
        print("\n💡 More examples:")
        print("  client.agent_chat('Complex question requiring reasoning')")
        print("  client.list_files('unstructured')")
        print("  client.list_databases()")
        print("  client.upload_file('path/to/file.pdf', 'unstructured', knowledge_base='my_kb')")
        
    except ValueError as e:
        print(f"❌ Configuration error: {e}")
        print("\n💡 Make sure to set your API key:")
        print("   export API_KEY='your-api-key-here'")
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()
