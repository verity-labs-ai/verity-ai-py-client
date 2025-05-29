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
from example import VerityAIExamples


def simple_chat_example():
    """Simple example of asking a question about unstructured data."""
    print("🔍 Simple Chat Example")
    print("-" * 40)
    
    # Initialize the SDK
    examples = VerityAIExamples()
    
    # Ask a simple question
    response = examples.unstructured_chat_completion(
        query="What are the main symptoms of COVID-19?",
        knowledge_base="all"
    )
    
    print("✅ Chat completed successfully!")
    return response


def simple_sql_example():
    """Simple example of asking a question about structured data."""
    print("\n🗄️ Simple SQL Example")
    print("-" * 40)
    
    # Initialize the SDK
    examples = VerityAIExamples()
    
    # Ask a question that will be converted to SQL
    response = examples.structured_chat_completion(
        query="How many patients are in the database?",
        database_name="veritydemo_mimic"
    )
    
    print("✅ SQL query completed successfully!")
    return response


def simple_file_listing_example():
    """Simple example of listing files in storage."""
    print("\n📁 Simple File Listing Example")
    print("-" * 40)
    
    # Initialize the SDK
    examples = VerityAIExamples()
    
    # List files in unstructured storage
    response = examples.list_files(
        storage_type="unstructured",
        page_size=10
    )
    
    print("✅ File listing completed successfully!")
    return response


def simple_document_search_example():
    """Simple example of searching for documents."""
    print("\n🔍 Simple Document Search Example")
    print("-" * 40)
    
    # Initialize the SDK
    examples = VerityAIExamples()
    
    # Search for relevant documents
    response = examples.retrieve_documents(
        query="patient treatment protocols",
        top_k=5
    )
    
    print("✅ Document search completed successfully!")
    return response


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