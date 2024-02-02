from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AddChunkToGroupData")


@_attrs_define
class AddChunkToGroupData:
    """
    Attributes:
        chunk_id (str): Id of the chunk to make a member of the group. Think of this as "bookmark"ing a chunk.
    """

    chunk_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        chunk_id = self.chunk_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chunk_id": chunk_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        chunk_id = d.pop("chunk_id")

        add_chunk_to_group_data = cls(
            chunk_id=chunk_id,
        )

        add_chunk_to_group_data.additional_properties = d
        return add_chunk_to_group_data

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
