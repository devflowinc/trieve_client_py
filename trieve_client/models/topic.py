import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="Topic")


@_attrs_define
class Topic:
    """
    Attributes:
        created_at (datetime.datetime):
        dataset_id (str):
        deleted (bool):
        id (str):
        name (str):
        updated_at (datetime.datetime):
        user_id (str):
    """

    created_at: datetime.datetime
    dataset_id: str
    deleted: bool
    id: str
    name: str
    updated_at: datetime.datetime
    user_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        dataset_id = self.dataset_id

        deleted = self.deleted

        id = self.id

        name = self.name

        updated_at = self.updated_at.isoformat()

        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "dataset_id": dataset_id,
                "deleted": deleted,
                "id": id,
                "name": name,
                "updated_at": updated_at,
                "user_id": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = isoparse(d.pop("created_at"))

        dataset_id = d.pop("dataset_id")

        deleted = d.pop("deleted")

        id = d.pop("id")

        name = d.pop("name")

        updated_at = isoparse(d.pop("updated_at"))

        user_id = d.pop("user_id")

        topic = cls(
            created_at=created_at,
            dataset_id=dataset_id,
            deleted=deleted,
            id=id,
            name=name,
            updated_at=updated_at,
            user_id=user_id,
        )

        topic.additional_properties = d
        return topic

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
