from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.slim_group import SlimGroup


T = TypeVar("T", bound="BookmarkGroupResult")


@_attrs_define
class BookmarkGroupResult:
    """
    Attributes:
        chunk_uuid (str):
        slim_groups (List['SlimGroup']):
    """

    chunk_uuid: str
    slim_groups: List["SlimGroup"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        chunk_uuid = self.chunk_uuid

        slim_groups = []
        for slim_groups_item_data in self.slim_groups:
            slim_groups_item = slim_groups_item_data.to_dict()
            slim_groups.append(slim_groups_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chunk_uuid": chunk_uuid,
                "slim_groups": slim_groups,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.slim_group import SlimGroup

        d = src_dict.copy()
        chunk_uuid = d.pop("chunk_uuid")

        slim_groups = []
        _slim_groups = d.pop("slim_groups")
        for slim_groups_item_data in _slim_groups:
            slim_groups_item = SlimGroup.from_dict(slim_groups_item_data)

            slim_groups.append(slim_groups_item)

        bookmark_group_result = cls(
            chunk_uuid=chunk_uuid,
            slim_groups=slim_groups,
        )

        bookmark_group_result.additional_properties = d
        return bookmark_group_result

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
