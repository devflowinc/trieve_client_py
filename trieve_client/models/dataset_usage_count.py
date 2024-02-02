from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DatasetUsageCount")


@_attrs_define
class DatasetUsageCount:
    """
    Attributes:
        chunk_count (int):
        dataset_id (str):
        id (str):
    """

    chunk_count: int
    dataset_id: str
    id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        chunk_count = self.chunk_count

        dataset_id = self.dataset_id

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chunk_count": chunk_count,
                "dataset_id": dataset_id,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        chunk_count = d.pop("chunk_count")

        dataset_id = d.pop("dataset_id")

        id = d.pop("id")

        dataset_usage_count = cls(
            chunk_count=chunk_count,
            dataset_id=dataset_id,
            id=id,
        )

        dataset_usage_count.additional_properties = d
        return dataset_usage_count

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
