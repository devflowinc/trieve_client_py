from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RecommendChunksRequest")


@_attrs_define
class RecommendChunksRequest:
    """
    Attributes:
        positive_chunk_ids (List[str]): The ids of the chunks to be used as positive examples for the recommendation.
            The chunks in this array will be used to find similar chunks.
    """

    positive_chunk_ids: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        positive_chunk_ids = self.positive_chunk_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "positive_chunk_ids": positive_chunk_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        positive_chunk_ids = cast(List[str], d.pop("positive_chunk_ids"))

        recommend_chunks_request = cls(
            positive_chunk_ids=positive_chunk_ids,
        )

        recommend_chunks_request.additional_properties = d
        return recommend_chunks_request

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
