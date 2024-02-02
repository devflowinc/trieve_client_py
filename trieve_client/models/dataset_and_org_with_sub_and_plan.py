from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dataset import Dataset
    from ..models.organization_with_sub_and_plan import OrganizationWithSubAndPlan


T = TypeVar("T", bound="DatasetAndOrgWithSubAndPlan")


@_attrs_define
class DatasetAndOrgWithSubAndPlan:
    """
    Attributes:
        dataset (Dataset):
        organization (OrganizationWithSubAndPlan):
    """

    dataset: "Dataset"
    organization: "OrganizationWithSubAndPlan"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dataset = self.dataset.to_dict()

        organization = self.organization.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataset": dataset,
                "organization": organization,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dataset import Dataset
        from ..models.organization_with_sub_and_plan import OrganizationWithSubAndPlan

        d = src_dict.copy()
        dataset = Dataset.from_dict(d.pop("dataset"))

        organization = OrganizationWithSubAndPlan.from_dict(d.pop("organization"))

        dataset_and_org_with_sub_and_plan = cls(
            dataset=dataset,
            organization=organization,
        )

        dataset_and_org_with_sub_and_plan.additional_properties = d
        return dataset_and_org_with_sub_and_plan

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
