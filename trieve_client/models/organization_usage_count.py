from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OrganizationUsageCount")


@_attrs_define
class OrganizationUsageCount:
    """
    Attributes:
        dataset_count (int):
        file_storage (int):
        id (str):
        message_count (int):
        org_id (str):
        user_count (int):
    """

    dataset_count: int
    file_storage: int
    id: str
    message_count: int
    org_id: str
    user_count: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dataset_count = self.dataset_count

        file_storage = self.file_storage

        id = self.id

        message_count = self.message_count

        org_id = self.org_id

        user_count = self.user_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataset_count": dataset_count,
                "file_storage": file_storage,
                "id": id,
                "message_count": message_count,
                "org_id": org_id,
                "user_count": user_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dataset_count = d.pop("dataset_count")

        file_storage = d.pop("file_storage")

        id = d.pop("id")

        message_count = d.pop("message_count")

        org_id = d.pop("org_id")

        user_count = d.pop("user_count")

        organization_usage_count = cls(
            dataset_count=dataset_count,
            file_storage=file_storage,
            id=id,
            message_count=message_count,
            org_id=org_id,
            user_count=user_count,
        )

        organization_usage_count.additional_properties = d
        return organization_usage_count

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
