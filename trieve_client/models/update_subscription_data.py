from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateSubscriptionData")


@_attrs_define
class UpdateSubscriptionData:
    """
    Attributes:
        plan_id (str):
        subscription_id (str):
    """

    plan_id: str
    subscription_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        plan_id = self.plan_id

        subscription_id = self.subscription_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plan_id": plan_id,
                "subscription_id": subscription_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        plan_id = d.pop("plan_id")

        subscription_id = d.pop("subscription_id")

        update_subscription_data = cls(
            plan_id=plan_id,
            subscription_id=subscription_id,
        )

        update_subscription_data.additional_properties = d
        return update_subscription_data

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
