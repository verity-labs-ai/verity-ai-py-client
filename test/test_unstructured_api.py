# coding: utf-8

"""
    AI Labs API Service

    Comprehensive API service for unstructured and structured RAG generation, file management, UI interactions, ground truth generation, and evaluation

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from verity_ai_pyc.api.unstructured_api import UnstructuredApi


class TestUnstructuredApi(unittest.TestCase):
    """UnstructuredApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UnstructuredApi()

    def tearDown(self) -> None:
        pass

    def test_list_kb_documents(self) -> None:
        """Test case for list_kb_documents

        list knowledge base documents
        """
        pass

    def test_retrieve(self) -> None:
        """Test case for retrieve

        retrieve unstructured data
        """
        pass

    def test_validate_ingestion_rag_generation_validate_ingestion_post(self) -> None:
        """Test case for validate_ingestion_rag_generation_validate_ingestion_post

        Validate ingestion status of uploaded documents
        """
        pass


if __name__ == '__main__':
    unittest.main()
