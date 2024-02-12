from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecommendChunksRequest")


@_attrs_define
class RecommendChunksRequest:
    """
    Attributes:
        positive_chunk_ids (List[str]): The ids of the chunks to be used as positive examples for the recommendation.
            The chunks in this array will be used to find similar chunks.
        limit (Union[None, Unset, int]): The number of chunks to return. This is the number of chunks which will be
            returned in the response. The default is 10.
    """

    positive_chunk_ids: List[str]
    limit: Union[None, Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        positive_chunk_ids = self.positive_chunk_ids

        limit: Union[None, Unset, int]
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "positive_chunk_ids": positive_chunk_ids,
            }
        )
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        positive_chunk_ids = cast(List[str], d.pop("positive_chunk_ids"))

        def _parse_limit(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        limit = _parse_limit(d.pop("limit", UNSET))

        recommend_chunks_request = cls(
            positive_chunk_ids=positive_chunk_ids,
            limit=limit,
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
