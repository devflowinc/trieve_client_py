from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetGroupsForChunksData")


@_attrs_define
class GetGroupsForChunksData:
    """
    Attributes:
        chunk_ids (List[str]):
    """

    chunk_ids: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        chunk_ids = self.chunk_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chunk_ids": chunk_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        chunk_ids = cast(List[str], d.pop("chunk_ids"))

        get_groups_for_chunks_data = cls(
            chunk_ids=chunk_ids,
        )

        get_groups_for_chunks_data.additional_properties = d
        return get_groups_for_chunks_data

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
