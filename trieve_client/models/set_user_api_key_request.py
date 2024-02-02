from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SetUserApiKeyRequest")


@_attrs_define
class SetUserApiKeyRequest:
    """
    Attributes:
        name (str): The name which will be assigned to the new api key.
        role (int): The role which will be assigned to the new api key. Either 0 (read), 1 (read and write at the level
            of the currently auth'ed user). The auth'ed user must have a role greater than or equal to the role being
            assigned which means they must be an admin (1) or owner (2) of the organization to assign write permissions with
            a role of 1.
    """

    name: str
    role: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        role = self.role

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        role = d.pop("role")

        set_user_api_key_request = cls(
            name=name,
            role=role,
        )

        set_user_api_key_request.additional_properties = d
        return set_user_api_key_request

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
