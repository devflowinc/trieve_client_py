import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stripe_plan import StripePlan
    from ..models.stripe_subscription import StripeSubscription


T = TypeVar("T", bound="OrganizationWithSubAndPlan")


@_attrs_define
class OrganizationWithSubAndPlan:
    """
    Attributes:
        created_at (datetime.datetime):
        id (str):
        name (str):
        updated_at (datetime.datetime):
        plan (Union['StripePlan', None, Unset]):
        registerable (Union[None, Unset, bool]):
        subscription (Union['StripeSubscription', None, Unset]):
    """

    created_at: datetime.datetime
    id: str
    name: str
    updated_at: datetime.datetime
    plan: Union["StripePlan", None, Unset] = UNSET
    registerable: Union[None, Unset, bool] = UNSET
    subscription: Union["StripeSubscription", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.stripe_plan import StripePlan
        from ..models.stripe_subscription import StripeSubscription

        created_at = self.created_at.isoformat()

        id = self.id

        name = self.name

        updated_at = self.updated_at.isoformat()

        plan: Union[Dict[str, Any], None, Unset]
        if isinstance(self.plan, Unset):
            plan = UNSET
        elif isinstance(self.plan, StripePlan):
            plan = self.plan.to_dict()
        else:
            plan = self.plan

        registerable: Union[None, Unset, bool]
        if isinstance(self.registerable, Unset):
            registerable = UNSET
        else:
            registerable = self.registerable

        subscription: Union[Dict[str, Any], None, Unset]
        if isinstance(self.subscription, Unset):
            subscription = UNSET
        elif isinstance(self.subscription, StripeSubscription):
            subscription = self.subscription.to_dict()
        else:
            subscription = self.subscription

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "name": name,
                "updated_at": updated_at,
            }
        )
        if plan is not UNSET:
            field_dict["plan"] = plan
        if registerable is not UNSET:
            field_dict["registerable"] = registerable
        if subscription is not UNSET:
            field_dict["subscription"] = subscription

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stripe_plan import StripePlan
        from ..models.stripe_subscription import StripeSubscription

        d = src_dict.copy()
        created_at = isoparse(d.pop("created_at"))

        id = d.pop("id")

        name = d.pop("name")

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_plan(data: object) -> Union["StripePlan", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                plan_type_1 = StripePlan.from_dict(data)

                return plan_type_1
            except:  # noqa: E722
                pass
            return cast(Union["StripePlan", None, Unset], data)

        plan = _parse_plan(d.pop("plan", UNSET))

        def _parse_registerable(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        registerable = _parse_registerable(d.pop("registerable", UNSET))

        def _parse_subscription(data: object) -> Union["StripeSubscription", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                subscription_type_1 = StripeSubscription.from_dict(data)

                return subscription_type_1
            except:  # noqa: E722
                pass
            return cast(Union["StripeSubscription", None, Unset], data)

        subscription = _parse_subscription(d.pop("subscription", UNSET))

        organization_with_sub_and_plan = cls(
            created_at=created_at,
            id=id,
            name=name,
            updated_at=updated_at,
            plan=plan,
            registerable=registerable,
            subscription=subscription,
        )

        organization_with_sub_and_plan.additional_properties = d
        return organization_with_sub_and_plan

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
