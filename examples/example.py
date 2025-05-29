#!/usr/bin/env python3
"""
Simple Verity AI SDK Usage Examples

This file shows simple, focused examples of how to use individual endpoints
with the Verity AI Python SDK.

Prerequisites:
1. Install the SDK: pip install -e .
2. Set your API key: export API_KEY="your-api-key-here"

Usage:
    python simple_usage.py
"""

import os
import verity_ai_pyc
from verity_ai_pyc.rest import ApiException
import dotenv

## update this to the path of the .env file
dotenv.load_dotenv("../../.env")

def simple_chat_example():
    """Simple example of chat completion."""
    print("\n💬 Simple Chat Example")
    print("-" * 40)
    
    # Configure the client
    configuration = verity_ai_pyc.Configuration(
        host="https://chat.veritylabs.ai"
    )
    configuration.api_key['XAPIKeyAuth'] = os.environ["API_KEY"]

    # Create API client
    with verity_ai_pyc.ApiClient(configuration) as api_client:
        # Create a chat completion
        completions_api = verity_ai_pyc.CompletionsApi(api_client)

        # Use Message class instead of ChatCompletionMessage for the request
        chat_request = verity_ai_pyc.ChatCompletionRequestPublic(
            model="anthropic_claude_3_5_sonnet_v1",
            messages=[
                verity_ai_pyc.Message(  # Fixed: Use Message instead of ChatCompletionMessage
                    role="user",
                    content="What is artificial intelligence?"
                )
            ],
            data_type="unstructured",  # Added required field
            knowledge_base="all"  # Added knowledge base
        )

        try:
            response = completions_api.create_chat_completion_rag_generation_chat_completions_post(chat_request)
            print("✅ AI Response:", response.messages[0].content)  # Fixed: access messages[0].content
            return response
        except ApiException as e:
            print(f"❌ Error: {e}")
            return None

def simple_models_example():
    """Simple example of listing models."""
    print("\n🔍 Simple Models Example")
    print("-" * 40)
    
    # Configure the client
    configuration = verity_ai_pyc.Configuration(
        host="https://chat.veritylabs.ai"
    )
    configuration.api_key['XAPIKeyAuth'] = os.environ["API_KEY"]

    # Create API client
    with verity_ai_pyc.ApiClient(configuration) as api_client:
        # List available models
        models_api = verity_ai_pyc.ModelsApi(api_client)
        try:
            models = models_api.list_models_rag_generation_models_get()
            print(f"✅ Available models: {models}")
            return models
        except ApiException as e:
            print(f"❌ Error: {e}")
            return None

def simple_sql_example():
    """Simple example of SQL chat."""
    print("\n🗄️ Simple SQL Example")
    print("-" * 40)
    
    # Configure the client
    configuration = verity_ai_pyc.Configuration(
        host="https://chat.veritylabs.ai"
    )
    configuration.api_key['XAPIKeyAuth'] = os.environ["API_KEY"]

    # Create API client
    with verity_ai_pyc.ApiClient(configuration) as api_client:
        completions_api = verity_ai_pyc.CompletionsApi(api_client)

        chat_request = verity_ai_pyc.ChatCompletionRequestPublic(
            model="anthropic_claude_3_5_sonnet_v1",
            messages=[
                verity_ai_pyc.Message(
                    role="user",
                    content="How many records are in the database?"
                )
            ],
            data_type="structured",
            database_name="veritydemo_mimic"
        )

        try:
            response = completions_api.create_chat_completion_rag_generation_chat_completions_post(chat_request)
            print("✅ SQL Response:", response.messages[0].content)
            return response
        except ApiException as e:
            print(f"❌ Error: {e}")
            return None

def simple_file_listing_example():
    """Simple example of listing files."""
    print("\n📁 Simple File Listing Example")
    print("-" * 40)
    
    # Configure the client
    configuration = verity_ai_pyc.Configuration(
        host="https://chat.veritylabs.ai"
    )
    configuration.api_key['XAPIKeyAuth'] = os.environ["API_KEY"]

    # Create API client
    with verity_ai_pyc.ApiClient(configuration) as api_client:
        file_management_api = verity_ai_pyc.FileManagementApi(api_client)
        
        try:
            response = file_management_api.list_files_get_fileman_data_list_get(
                storage_type="unstructured",
                page=1,
                page_size=5
            )
            print(f"✅ Found {len(response.files)} files:")
            for i, file_info in enumerate(response.files[:3], 1):
                print(f"   {i}. {file_info.filename} ({file_info.size_mb:.2f} MB)")
            return response
        except ApiException as e:
            print(f"❌ Error: {e}")
            return None

def simple_document_search_example():
    """Simple example of searching for documents."""
    print("\n🔍 Simple Document Search Example")
    print("-" * 40)
    
    # Configure the client
    configuration = verity_ai_pyc.Configuration(
        host="https://chat.veritylabs.ai"
    )
    configuration.api_key['XAPIKeyAuth'] = os.environ["API_KEY"]

    # Create API client
    with verity_ai_pyc.ApiClient(configuration) as api_client:
        unstructured_api = verity_ai_pyc.UnstructuredApi(api_client)
        
        try:
            # Create retrieval request
            request = verity_ai_pyc.RetrievalRequestPublic(
                query="apple",
                knowledge_base="all",
                top_k=5
            )
            
            response = unstructured_api.retrieve(request)
            print("✅ Document search completed successfully!")
            return response
        except ApiException as e:
            print(f"❌ Error: {e}")
            return None

def main():
    """Run simple examples."""
    print("🚀 Verity AI SDK - Simple Usage Examples")
    print("=" * 50)
    
    try:
        # Check if API key is set
        if not os.getenv("API_KEY"):
            print("❌ Error: API_KEY environment variable not set")
            print("💡 Set your API key: export API_KEY='your-api-key-here'")
            return
        
        # Run simple examples
        simple_models_example()
        simple_chat_example()
        simple_sql_example()
        simple_file_listing_example()
        simple_document_search_example()
        
        print("\n" + "=" * 50)
        print("✅ All simple examples completed!")
        print("\n💡 For more advanced examples, see example.py")
        
    except Exception as e:
        print(f"❌ Error running examples: {e}")
        print("\n💡 Make sure:")
        print("   1. Your API key is valid")
        print("   2. You have access to the knowledge bases and databases used")
        print("   3. The SDK is properly installed")


if __name__ == "__main__":
    main() 