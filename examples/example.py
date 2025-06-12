#!/usr/bin/env python3
"""
Simple Verity AI SDK Usage Examples

This file shows simple, focused examples of how to use individual endpoints
with the Verity AI Python SDK.

Prerequisites:
1. Install the SDK: pip install -e .
2. Set your API key: export API_KEY="your-api-key-here"
3. For agent examples: Create agents in the UI first, then use their IDs

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
            knowledge_base=verity_ai_pyc.KnowledgeBase("all")  # Pass as KnowledgeBase object
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
                knowledge_base=verity_ai_pyc.KnowledgeBase1("all"),  # Use KnowledgeBase1 for RetrievalRequestPublic
                top_k=5
            )
            
            response = unstructured_api.retrieve(request)
            print("✅ Document search completed successfully!")
            return response
        except ApiException as e:
            print(f"❌ Error: {e}")
            return None

def simple_list_agents_example():
    """Simple example of listing available agents."""
    print("\n🤖 Simple List Agents Example")
    print("-" * 40)
    
    # Configure the client
    configuration = verity_ai_pyc.Configuration(
        host="https://chat.veritylabs.ai"
    )
    configuration.api_key['XAPIKeyAuth'] = os.environ["API_KEY"]

    # Create API client
    with verity_ai_pyc.ApiClient(configuration) as api_client:
        agents_api = verity_ai_pyc.AgentsApi(api_client)
        
        try:
            # List all active agents using the proper endpoint
            # Based on the API documentation, the method name is list_agents_endpoint_v1_agents_get
            agents = agents_api.list_agents_endpoint_v1_agents_get()
            
            if not agents:
                print("📭 No agents found")
                return []
            
            print(f"✅ Found {len(agents)} agents:")
            
            # Display detailed information for each agent
            for i, agent in enumerate(agents, 1):
                print(f"\n   {i}. Agent: {agent.name}")
                print(f"      • ID: {agent.agent_id}")
                print(f"      • Origin: {agent.agent_origin}")
                print(f"      • Model: {agent.model}")
                
                # Display additional attributes if available
                if hasattr(agent, 'description') and agent.description:
                    print(f"      • Description: {agent.description}")
                if hasattr(agent, 'created_at') and agent.created_at:
                    print(f"      • Created: {agent.created_at}")
                if hasattr(agent, 'status') and agent.status:
                    print(f"      • Status: {agent.status}")
                
                # Limit display to first 5 agents for readability
                if i >= 5:
                    remaining = len(agents) - 5
                    if remaining > 0:
                        print(f"\n   ... and {remaining} more agents")
                    break
                
            return agents
        except ApiException as e:
            print(f"❌ Error listing agents: {e}")
            print("💡 Make sure you have access to the agents API")
            return None
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            return None

def simple_agent_chat_example():
    """Simple example of agent chat using agent_flag=True and agent_id."""
    print("\n🤖 Simple Agent Chat Example")
    print("-" * 40)
    
    configuration = verity_ai_pyc.Configuration(host="https://chat.veritylabs.ai")
    configuration.api_key['XAPIKeyAuth'] = os.environ["API_KEY"]

    with verity_ai_pyc.ApiClient(configuration) as api_client:
        completions_api = verity_ai_pyc.CompletionsApi(api_client)
        
        # Example with a specific agent ID (replace with your actual agent ID)
        agent_id = "CUS_d551e1ae-3792-423f-950c-bc3a2ef5680e"  # Get this from UI or list agents endpoint
        
        chat_request = verity_ai_pyc.ChatCompletionRequestPublic(
            model="anthropic_claude_3_5_sonnet_v1",
            messages=[verity_ai_pyc.Message(role="user", content="Hello! What can you help me with?")],
            agent_flag=True,  # Enable agent mode
            agent_id=agent_id,  # Specify which agent to use
            data_type="unstructured",
            knowledge_base=verity_ai_pyc.KnowledgeBase("all")  # Pass as KnowledgeBase object
        )

        try:
            response = completions_api.create_chat_completion_rag_generation_chat_completions_post(chat_request)
            print("✅ Agent Response:", response.messages[0].content)
            return response
        except ApiException as e:
            print(f"❌ Error: {e}")
            print("💡 Make sure to replace 'CUS_your_agent_id_here' with a real agent ID")
            return None

def simple_upload_unstructured_example():
    """Simple example of uploading an unstructured file."""
    print("\n📤 Simple Upload Unstructured File Example")
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
            # Create a simple text file for demonstration
            file_content = b"This is a test document for Verity AI SDK demonstration."
            filename = "sdk_test_document.txt"
            
            response = file_management_api.upload_file_fileman_data_upload_post(
                file=(filename, file_content),
                storage_type="unstructured",
                knowledge_base="test_knowledge_base"  # This is likely a string parameter for upload
            )
            
            print(f"✅ Successfully uploaded {filename}")
            print(f"Response: {response}")
            return response
        except ApiException as e:
            print(f"❌ Error uploading file: {e}")
            return None

def simple_upload_structured_example():
    """Simple example of uploading a structured file."""
    print("\n📤 Simple Upload Structured File Example")
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
            # Create a simple CSV file for demonstration
            csv_content = b"id,name,value\n1,Test Item,100\n2,Another Item,200"
            filename = "sdk_test_data.csv"
            
            response = file_management_api.upload_file_fileman_data_upload_post(
                file=(filename, csv_content),
                storage_type="structured",
                database_name="test_db",
                table_name="test_table"
            )
            
            print(f"✅ Successfully uploaded {filename}")
            print(f"Response: {response}")
            return response
        except ApiException as e:
            print(f"❌ Error uploading structured file: {e}")
            return None

def simple_delete_unstructured_example():
    """Simple example of deleting an unstructured file."""
    print("\n🗑️ Simple Delete Unstructured File Example")
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
            # Create delete request
            delete_request = verity_ai_pyc.DeleteRequest(
                filenames=["sdk_test_document.txt"]
            )
            
            response = file_management_api.delete_files_fileman_data_delete_delete(
                storage_type="unstructured",
                delete_request=delete_request,
                base_path="test_knowledge_base"
            )
            
            print("✅ Successfully deleted unstructured file")
            print(f"Response: {response}")
            return response
        except ApiException as e:
            print(f"❌ Error deleting unstructured file: {e}")
            return None

def simple_delete_structured_example():
    """Simple example of deleting a structured file."""
    print("\n🗑️ Simple Delete Structured File Example")
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
            # Create delete request
            delete_request = verity_ai_pyc.DeleteRequest(
                filenames=["sdk_test_data.csv"]
            )
            
            response = file_management_api.delete_files_fileman_data_delete_delete(
                storage_type="structured",
                delete_request=delete_request,
                base_path="test_db",
                sub_path="test_table"
            )
            
            print("✅ Successfully deleted structured file")
            print(f"Response: {response}")
            return response
        except ApiException as e:
            print(f"❌ Error deleting structured file: {e}")
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
        # File management examples
        print("\n" + "=" * 30)
        print("📁 File Management Examples")
        print("=" * 30)
        
        simple_upload_unstructured_example()
        simple_upload_structured_example()
        simple_delete_unstructured_example()
        simple_delete_structured_example()
                
        # Run simple examples
        print("\n" + "=" * 30)
        print("� Simple Examples")
        print("=" * 30)
        simple_models_example()
        simple_chat_example()
        simple_sql_example()
        simple_file_listing_example()
        simple_document_search_example()
        
        # Agent examples
        print("\n" + "=" * 30)
        print("🤖 Agent Examples")
        print("=" * 30)
        
        # simple_list_agents_example()
        simple_agent_chat_example()
        

        
        print("\n" + "=" * 50)
        print("✅ All simple examples completed!")
        print("\n💡 For more advanced examples, see the examples notebook")
        
    except Exception as e:
        print(f"❌ Error running examples: {e}")
        print("\n💡 Make sure:")
        print("   1. Your API key is valid")
        print("   2. You have access to the knowledge bases and databases used")
        print("   3. The SDK is properly installed")


if __name__ == "__main__":
    main() 