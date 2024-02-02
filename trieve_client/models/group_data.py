from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.chunk_group_and_file import ChunkGroupAndFile


T = TypeVar("T", bound="GroupData")


@_attrs_define
class GroupData:
    """
    Attributes:
        groups (List['ChunkGroupAndFile']):
        total_pages (int):
    """

    groups: List["ChunkGroupAndFile"]
    total_pages: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        groups = []
        for groups_item_data in self.groups:
            groups_item = groups_item_data.to_dict()
            groups.append(groups_item)

        total_pages = self.total_pages

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "groups": groups,
                "total_pages": total_pages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.chunk_group_and_file import ChunkGroupAndFile

        d = src_dict.copy()
        groups = []
        _groups = d.pop("groups")
        for groups_item_data in _groups:
            groups_item = ChunkGroupAndFile.from_dict(groups_item_data)

            groups.append(groups_item)

        total_pages = d.pop("total_pages")

        group_data = cls(
            groups=groups,
            total_pages=total_pages,
        )

        group_data.additional_properties = d
        return group_data

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
