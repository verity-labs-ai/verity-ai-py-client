# coding: utf-8

"""
    AI Labs API Service

    Comprehensive API service for unstructured and structured RAG generation, file management, UI interactions, ground truth generation, and evaluation

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from verity_ai_pyc.models.agent_update_public import AgentUpdatePublic

class TestAgentUpdatePublic(unittest.TestCase):
    """AgentUpdatePublic unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AgentUpdatePublic:
        """Test AgentUpdatePublic
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AgentUpdatePublic`
        """
        model = AgentUpdatePublic()
        if include_optional:
            return AgentUpdatePublic(
                name = '',
                description = '',
                model = '',
                system_prompt = '',
                custom_prompt = '',
                allowed_tools = [
                    ''
                    ],
                use_mcp = True,
                mcp_server_urls = [
                    ''
                    ],
                agent_strategy = '',
                stream = True,
                active = True,
                agent_origin = '',
                parent_agent_id = '',
                knowledge_base = '',
                database_name = '',
                table_name = '',
                max_trials = 1.0
            )
        else:
            return AgentUpdatePublic(
        )
        """

    def testAgentUpdatePublic(self):
        """Test AgentUpdatePublic"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
