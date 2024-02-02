import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="Event")


@_attrs_define
class Event:
    """
    Attributes:
        created_at (datetime.datetime):
        dataset_id (str):
        event_data (Any):
        event_type (str):
        id (str):
        updated_at (datetime.datetime):
    """

    created_at: datetime.datetime
    dataset_id: str
    event_data: Any
    event_type: str
    id: str
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        dataset_id = self.dataset_id

        event_data = self.event_data

        event_type = self.event_type

        id = self.id

        updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "dataset_id": dataset_id,
                "event_data": event_data,
                "event_type": event_type,
                "id": id,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = isoparse(d.pop("created_at"))

        dataset_id = d.pop("dataset_id")

        event_data = d.pop("event_data")

        event_type = d.pop("event_type")

        id = d.pop("id")

        updated_at = isoparse(d.pop("updated_at"))

        event = cls(
            created_at=created_at,
            dataset_id=dataset_id,
            event_data=event_data,
            event_type=event_type,
            id=id,
            updated_at=updated_at,
        )

        event.additional_properties = d
        return event

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
