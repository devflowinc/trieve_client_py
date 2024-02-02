from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetUserWithChunksData")


@_attrs_define
class GetUserWithChunksData:
    """
    Attributes:
        page (int): The page of chunks to fetch. Each page is 10 chunks. Support for custom page size is coming soon.
        user_id (str): The id of the user to fetch the chunks for.
    """

    page: int
    user_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        page = self.page

        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page": page,
                "user_id": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        page = d.pop("page")

        user_id = d.pop("user_id")

        get_user_with_chunks_data = cls(
            page=page,
            user_id=user_id,
        )

        get_user_with_chunks_data.additional_properties = d
        return get_user_with_chunks_data

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
