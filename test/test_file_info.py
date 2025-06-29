# coding: utf-8

"""
    AI Labs API Service

    Comprehensive API service for unstructured and structured RAG generation, file management, UI interactions, ground truth generation, and evaluation

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from verity_ai_pyc.models.file_info import FileInfo

class TestFileInfo(unittest.TestCase):
    """FileInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FileInfo:
        """Test FileInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FileInfo`
        """
        model = FileInfo()
        if include_optional:
            return FileInfo(
                filename = '',
                size_bytes = 56,
                size_mb = 1.337,
                file_type = '',
                uploaded_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                is_directory = True
            )
        else:
            return FileInfo(
                filename = '',
                size_bytes = 56,
                size_mb = 1.337,
                file_type = '',
                uploaded_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testFileInfo(self):
        """Test FileInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
