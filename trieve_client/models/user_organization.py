import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="UserOrganization")


@_attrs_define
class UserOrganization:
    """
    Attributes:
        created_at (datetime.datetime):
        id (str):
        organization_id (str):
        role (int):
        updated_at (datetime.datetime):
        user_id (str):
    """

    created_at: datetime.datetime
    id: str
    organization_id: str
    role: int
    updated_at: datetime.datetime
    user_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        organization_id = self.organization_id

        role = self.role

        updated_at = self.updated_at.isoformat()

        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "organization_id": organization_id,
                "role": role,
                "updated_at": updated_at,
                "user_id": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = isoparse(d.pop("created_at"))

        id = d.pop("id")

        organization_id = d.pop("organization_id")

        role = d.pop("role")

        updated_at = isoparse(d.pop("updated_at"))

        user_id = d.pop("user_id")

        user_organization = cls(
            created_at=created_at,
            id=id,
            organization_id=organization_id,
            role=role,
            updated_at=updated_at,
            user_id=user_id,
        )

        user_organization.additional_properties = d
        return user_organization

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
