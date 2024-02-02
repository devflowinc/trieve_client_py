import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Organization")


@_attrs_define
class Organization:
    """
    Attributes:
        created_at (datetime.datetime):
        id (str):
        name (str):
        updated_at (datetime.datetime):
        registerable (Union[None, Unset, bool]):
    """

    created_at: datetime.datetime
    id: str
    name: str
    updated_at: datetime.datetime
    registerable: Union[None, Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        name = self.name

        updated_at = self.updated_at.isoformat()

        registerable: Union[None, Unset, bool]
        if isinstance(self.registerable, Unset):
            registerable = UNSET
        else:
            registerable = self.registerable

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "name": name,
                "updated_at": updated_at,
            }
        )
        if registerable is not UNSET:
            field_dict["registerable"] = registerable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = isoparse(d.pop("created_at"))

        id = d.pop("id")

        name = d.pop("name")

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_registerable(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        registerable = _parse_registerable(d.pop("registerable", UNSET))

        organization = cls(
            created_at=created_at,
            id=id,
            name=name,
            updated_at=updated_at,
            registerable=registerable,
        )

        organization.additional_properties = d
        return organization

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
