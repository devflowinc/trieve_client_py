import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="StripeSubscription")


@_attrs_define
class StripeSubscription:
    """
    Attributes:
        created_at (datetime.datetime):
        id (str):
        organization_id (str):
        plan_id (str):
        stripe_id (str):
        updated_at (datetime.datetime):
        current_period_end (Union[None, Unset, datetime.datetime]):
    """

    created_at: datetime.datetime
    id: str
    organization_id: str
    plan_id: str
    stripe_id: str
    updated_at: datetime.datetime
    current_period_end: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        organization_id = self.organization_id

        plan_id = self.plan_id

        stripe_id = self.stripe_id

        updated_at = self.updated_at.isoformat()

        current_period_end: Union[None, Unset, str]
        if isinstance(self.current_period_end, Unset):
            current_period_end = UNSET
        elif isinstance(self.current_period_end, datetime.datetime):
            current_period_end = self.current_period_end.isoformat()
        else:
            current_period_end = self.current_period_end

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "organization_id": organization_id,
                "plan_id": plan_id,
                "stripe_id": stripe_id,
                "updated_at": updated_at,
            }
        )
        if current_period_end is not UNSET:
            field_dict["current_period_end"] = current_period_end

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = isoparse(d.pop("created_at"))

        id = d.pop("id")

        organization_id = d.pop("organization_id")

        plan_id = d.pop("plan_id")

        stripe_id = d.pop("stripe_id")

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_current_period_end(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                current_period_end_type_0 = isoparse(data)

                return current_period_end_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        current_period_end = _parse_current_period_end(d.pop("current_period_end", UNSET))

        stripe_subscription = cls(
            created_at=created_at,
            id=id,
            organization_id=organization_id,
            plan_id=plan_id,
            stripe_id=stripe_id,
            updated_at=updated_at,
            current_period_end=current_period_end,
        )

        stripe_subscription.additional_properties = d
        return stripe_subscription

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
