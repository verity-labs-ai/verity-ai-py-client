# coding: utf-8

"""
    AI Labs API Service

    Comprehensive API service for unstructured and structured RAG generation, file management, UI interactions, ground truth generation, and evaluation

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from verity_ai_pyc.models.chat_completion_message import ChatCompletionMessage

class TestChatCompletionMessage(unittest.TestCase):
    """ChatCompletionMessage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChatCompletionMessage:
        """Test ChatCompletionMessage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChatCompletionMessage`
        """
        model = ChatCompletionMessage()
        if include_optional:
            return ChatCompletionMessage(
                role = '',
                content = '',
                metadata = {
                    'key' : null
                    }
            )
        else:
            return ChatCompletionMessage(
                role = '',
                content = '',
        )
        """

    def testChatCompletionMessage(self):
        """Test ChatCompletionMessage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
