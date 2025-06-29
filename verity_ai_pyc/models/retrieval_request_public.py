# coding: utf-8

"""
    AI Labs API Service

    Comprehensive API service for unstructured and structured RAG generation, file management, UI interactions, ground truth generation, and evaluation

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing_extensions import Annotated, Self
from verity_ai_pyc.models.knowledge_base1 import KnowledgeBase1


class RetrievalRequestPublic(BaseModel):
    """
    RetrievalRequestPublic
    """  # noqa: E501

    query: StrictStr = Field(description="The user query to retrieve documents for.")
    top_k: Optional[Annotated[int, Field(le=10, strict=True, ge=5)]] = Field(
        default=5, description="The number of top documents to retrieve (5-10)."
    )
    knowledge_base: Optional[KnowledgeBase1] = None
    __properties: ClassVar[List[str]] = ["query", "top_k", "knowledge_base"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of RetrievalRequestPublic from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of knowledge_base
        if self.knowledge_base:
            _dict["knowledge_base"] = self.knowledge_base.to_dict()
        # set to None if knowledge_base (nullable) is None
        # and model_fields_set contains the field
        if self.knowledge_base is None and "knowledge_base" in self.model_fields_set:
            _dict["knowledge_base"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RetrievalRequestPublic from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "query": obj.get("query"),
                "top_k": obj.get("top_k") if obj.get("top_k") is not None else 5,
                "knowledge_base": KnowledgeBase1.from_dict(obj["knowledge_base"])
                if obj.get("knowledge_base") is not None
                else None,
            }
        )
        return _obj
