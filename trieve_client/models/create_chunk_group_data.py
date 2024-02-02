from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateChunkGroupData")


@_attrs_define
class CreateChunkGroupData:
    """
    Attributes:
        description (str): Description to assign to the chunk_group. Convenience field for you to avoid having to
            remember what the group is for.
        name (str): Name to assign to the chunk_group. Does not need to be unique.
    """

    description: str
    name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description")

        name = d.pop("name")

        create_chunk_group_data = cls(
            description=description,
            name=name,
        )

        create_chunk_group_data.additional_properties = d
        return create_chunk_group_data

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
