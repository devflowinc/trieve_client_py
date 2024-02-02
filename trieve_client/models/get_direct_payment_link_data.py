from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetDirectPaymentLinkData")


@_attrs_define
class GetDirectPaymentLinkData:
    """
    Attributes:
        organization_id (str):
        plan_id (str):
    """

    organization_id: str
    plan_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        organization_id = self.organization_id

        plan_id = self.plan_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organization_id": organization_id,
                "plan_id": plan_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        organization_id = d.pop("organization_id")

        plan_id = d.pop("plan_id")

        get_direct_payment_link_data = cls(
            organization_id=organization_id,
            plan_id=plan_id,
        )

        get_direct_payment_link_data.additional_properties = d
        return get_direct_payment_link_data

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
