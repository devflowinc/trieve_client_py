from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SlimGroup")


@_attrs_define
class SlimGroup:
    """
    Attributes:
        dataset_id (str):
        id (str):
        name (str):
        of_current_dataset (bool):
    """

    dataset_id: str
    id: str
    name: str
    of_current_dataset: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dataset_id = self.dataset_id

        id = self.id

        name = self.name

        of_current_dataset = self.of_current_dataset

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataset_id": dataset_id,
                "id": id,
                "name": name,
                "of_current_dataset": of_current_dataset,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dataset_id = d.pop("dataset_id")

        id = d.pop("id")

        name = d.pop("name")

        of_current_dataset = d.pop("of_current_dataset")

        slim_group = cls(
            dataset_id=dataset_id,
            id=id,
            name=name,
            of_current_dataset=of_current_dataset,
        )

        slim_group.additional_properties = d
        return slim_group

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
