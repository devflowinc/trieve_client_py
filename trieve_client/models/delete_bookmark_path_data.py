from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteBookmarkPathData")


@_attrs_define
class DeleteBookmarkPathData:
    """
    Attributes:
        bookmark_id (str):
        group_id (str):
    """

    bookmark_id: str
    group_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bookmark_id = self.bookmark_id

        group_id = self.group_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bookmark_id": bookmark_id,
                "group_id": group_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bookmark_id = d.pop("bookmark_id")

        group_id = d.pop("group_id")

        delete_bookmark_path_data = cls(
            bookmark_id=bookmark_id,
            group_id=group_id,
        )

        delete_bookmark_path_data.additional_properties = d
        return delete_bookmark_path_data

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
