import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="StripePlan")


@_attrs_define
class StripePlan:
    """
    Attributes:
        amount (int):
        chunk_count (int):
        created_at (datetime.datetime):
        dataset_count (int):
        file_storage (int):
        id (str):
        message_count (int):
        name (str):
        stripe_id (str):
        updated_at (datetime.datetime):
        user_count (int):
    """

    amount: int
    chunk_count: int
    created_at: datetime.datetime
    dataset_count: int
    file_storage: int
    id: str
    message_count: int
    name: str
    stripe_id: str
    updated_at: datetime.datetime
    user_count: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount

        chunk_count = self.chunk_count

        created_at = self.created_at.isoformat()

        dataset_count = self.dataset_count

        file_storage = self.file_storage

        id = self.id

        message_count = self.message_count

        name = self.name

        stripe_id = self.stripe_id

        updated_at = self.updated_at.isoformat()

        user_count = self.user_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "chunk_count": chunk_count,
                "created_at": created_at,
                "dataset_count": dataset_count,
                "file_storage": file_storage,
                "id": id,
                "message_count": message_count,
                "name": name,
                "stripe_id": stripe_id,
                "updated_at": updated_at,
                "user_count": user_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount")

        chunk_count = d.pop("chunk_count")

        created_at = isoparse(d.pop("created_at"))

        dataset_count = d.pop("dataset_count")

        file_storage = d.pop("file_storage")

        id = d.pop("id")

        message_count = d.pop("message_count")

        name = d.pop("name")

        stripe_id = d.pop("stripe_id")

        updated_at = isoparse(d.pop("updated_at"))

        user_count = d.pop("user_count")

        stripe_plan = cls(
            amount=amount,
            chunk_count=chunk_count,
            created_at=created_at,
            dataset_count=dataset_count,
            file_storage=file_storage,
            id=id,
            message_count=message_count,
            name=name,
            stripe_id=stripe_id,
            updated_at=updated_at,
            user_count=user_count,
        )

        stripe_plan.additional_properties = d
        return stripe_plan

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
