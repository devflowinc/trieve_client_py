from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dataset_dto import DatasetDTO
    from ..models.dataset_usage_count import DatasetUsageCount


T = TypeVar("T", bound="DatasetAndUsage")


@_attrs_define
class DatasetAndUsage:
    """
    Attributes:
        dataset (DatasetDTO):
        dataset_usage (DatasetUsageCount):
    """

    dataset: "DatasetDTO"
    dataset_usage: "DatasetUsageCount"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dataset = self.dataset.to_dict()

        dataset_usage = self.dataset_usage.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataset": dataset,
                "dataset_usage": dataset_usage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dataset_dto import DatasetDTO
        from ..models.dataset_usage_count import DatasetUsageCount

        d = src_dict.copy()
        dataset = DatasetDTO.from_dict(d.pop("dataset"))

        dataset_usage = DatasetUsageCount.from_dict(d.pop("dataset_usage"))

        dataset_and_usage = cls(
            dataset=dataset,
            dataset_usage=dataset_usage,
        )

        dataset_and_usage.additional_properties = d
        return dataset_and_usage

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
