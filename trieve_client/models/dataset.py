import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="Dataset")


@_attrs_define
class Dataset:
    """
    Attributes:
        client_configuration (Any):
        created_at (datetime.datetime):
        id (str):
        name (str):
        organization_id (str):
        server_configuration (Any):
        updated_at (datetime.datetime):
    """

    client_configuration: Any
    created_at: datetime.datetime
    id: str
    name: str
    organization_id: str
    server_configuration: Any
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_configuration = self.client_configuration

        created_at = self.created_at.isoformat()

        id = self.id

        name = self.name

        organization_id = self.organization_id

        server_configuration = self.server_configuration

        updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "client_configuration": client_configuration,
                "created_at": created_at,
                "id": id,
                "name": name,
                "organization_id": organization_id,
                "server_configuration": server_configuration,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client_configuration = d.pop("client_configuration")

        created_at = isoparse(d.pop("created_at"))

        id = d.pop("id")

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        server_configuration = d.pop("server_configuration")

        updated_at = isoparse(d.pop("updated_at"))

        dataset = cls(
            client_configuration=client_configuration,
            created_at=created_at,
            id=id,
            name=name,
            organization_id=organization_id,
            server_configuration=server_configuration,
            updated_at=updated_at,
        )

        dataset.additional_properties = d
        return dataset

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
