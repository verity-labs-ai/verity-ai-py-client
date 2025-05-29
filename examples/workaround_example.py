#!/usr/bin/env python3
"""
Verity AI SDK Workaround Example

This file provides a workaround for the Optional[str] deserialization issue
in the generated SDK.
"""

import os
import json
from dotenv import load_dotenv
load_dotenv("../.env")

import verity_ai_pyc
from verity_ai_pyc.rest import ApiException

class VerityAIWorkaround:
    """
    Workaround class for the SDK type hint issue.
    """
    
    def __init__(self, api_key=None, base_url="https://chat.veritylabs.ai"):
        """Initialize with workaround for type hint issues."""
        self.api_key = api_key or os.getenv("API_KEY")
        if not self.api_key:
            raise ValueError("API key is required. Set API_KEY environment variable or pass api_key parameter.")
        
        # Configure the SDK
        self.configuration = verity_ai_pyc.Configuration(host=base_url)
        self.configuration.api_key['XAPIKeyAuth'] = self.api_key
        
        # Patch the problematic deserialization method
        self._patch_api_client()
        
        # Initialize API client
        self.api_client = verity_ai_pyc.ApiClient(self.configuration)
        
        # Initialize API instances
        self.models_api = verity_ai_pyc.ModelsApi(self.api_client)
        self.completions_api = verity_ai_pyc.CompletionsApi(self.api_client)
        self.unstructured_api = verity_ai_pyc.UnstructuredApi(self.api_client)
        self.structured_api = verity_ai_pyc.StructuredApi(self.api_client)
        self.file_management_api = verity_ai_pyc.FileManagementApi(self.api_client)
        
        print(f"✅ Verity AI SDK initialized with workaround")

    def _patch_api_client(self):
        """Patch the API client to handle type hint issues."""
        original_deserialize = verity_ai_pyc.ApiClient._ApiClient__deserialize
        
        def patched_deserialize(self, data, klass):
            """Patched deserialize method that handles type hints."""
            if isinstance(klass, str):
                # Handle problematic type hints
                if klass.startswith('Optional[') or '[' in klass:
                    # For Optional[str] or similar, just return the data as-is
                    if 'str' in klass:
                        return str(data) if data is not None else None
                    elif 'int' in klass:
                        return int(data) if data is not None else None
                    elif 'bool' in klass:
                        return bool(data) if data is not None else None
                    else:
                        return data
            
            # Call the original method for everything else
            return original_deserialize(self, data, klass)
        
        # Apply the patch
        verity_ai_pyc.ApiClient._ApiClient__deserialize = patched_deserialize

    def list_models(self):
        """List available models with error handling."""
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
            print(f"❌ API Error: {e}")
            raise
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            print(f"Raw response type: {type(models_response)}")
            print(f"Raw response: {repr(models_response)}")
            raise

    def simple_chat(self, query="What is COVID-19?", model=None):
        """Simple chat completion example."""
        print(f"\n💬 Simple chat completion...")
        print(f"   Query: {query}")
        
        try:
            # Get available models if none specified
            if model is None:
                models = self.list_models()
                model = models[0] if models else "anthropic_claude_3_haiku_v1"
            
            print(f"   Model: {model}")
            
            # Create request manually to avoid type issues
            request_data = {
                "model": model,
                "messages": [{"role": "user", "content": query}],
                "knowledge_base": "all",
                "data_type": "unstructured",
                "agent_flag": False,
                "stream": False
            }
            
            # Create the request object
            request = verity_ai_pyc.models.ChatCompletionRequestPublic(
                model=model,
                messages=[verity_ai_pyc.models.Message(role="user", content=query)],
                knowledge_base="all",
                data_type="unstructured",
                agent_flag=False,
                stream=False
            )
            
            # Call the API
            response = self.completions_api.create_chat_completion_rag_generation_chat_completions_post(request)
            
            print("✅ Response received:")
            print(f"   ID: {response.id}")
            print(f"   Model: {response.model}")
            
            if response.messages:
                assistant_message = response.messages[0]
                print(f"\n📝 Assistant Response:")
                print(f"   {assistant_message.content}")
            
            return response
            
        except Exception as e:
            print(f"❌ Error in chat completion: {e}")
            raise

    def list_files_simple(self, storage_type="unstructured"):
        """Simple file listing example."""
        print(f"\n📁 Listing files ({storage_type})...")
        
        try:
            response = self.file_management_api.list_files_get_fileman_data_list_get(
                storage_type=storage_type,
                page=1,
                page_size=10
            )
            
            print(f"✅ Found {len(response.files)} files:")
            for i, file_info in enumerate(response.files[:5], 1):
                print(f"   {i}. {file_info.filename} ({file_info.size_mb:.2f} MB)")
            
            return response
            
        except Exception as e:
            print(f"❌ Error listing files: {e}")
            raise

    def list_databases(self):
        """List database tables."""
        print(f"\n🗄️ Listing databases...")
        
        try:
            response = self.structured_api.list_db_tables_unstructured()
            
            print("✅ Databases found:")
            if isinstance(response, dict):
                for db_name, tables in response.items():
                    print(f"   🗃️ {db_name}: {len(tables) if isinstance(tables, list) else 'N/A'} tables")
            
            return response
            
        except Exception as e:
            print(f"❌ Error listing databases: {e}")
            raise


def main():
    """Test the workaround."""
    try:
        # Initialize with workaround
        client = VerityAIWorkaround()
        
        # Test basic functionality
        print("🧪 Testing basic functionality...")
        
        # 1. List models
        models = client.list_models()
        
        # 2. Simple chat
        if models:
            client.simple_chat("What is artificial intelligence?", models[0])
        
        # 3. List files
        client.list_files_simple("unstructured")
        
        # 4. List databases
        client.list_databases()
        
        print("\n✅ Workaround tests completed!")
        
    except Exception as e:
        print(f"❌ Workaround failed: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main() 