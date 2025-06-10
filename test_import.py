#!/usr/bin/env python3
"""
Simple test to verify the SDK can be imported
"""

try:
    import verity_ai_pyc
    print("✓ SDK import successful")
    print(f"✓ Package version: {getattr(verity_ai_pyc, '__version__', 'unknown')}")
    
    # Test importing main components
    from verity_ai_pyc import ApiClient, Configuration
    from verity_ai_pyc.api.completions_api import CompletionsApi
    print("✓ Main components imported successfully")
    
    print("\n🎉 SDK is ready to use!")
    
except ImportError as e:
    print(f"✗ Import failed: {e}")
    exit(1)
except Exception as e:
    print(f"✗ Unexpected error: {e}")
    exit(1)
