from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.event import Event


T = TypeVar("T", bound="EventReturn")


@_attrs_define
class EventReturn:
    """
    Attributes:
        event (List['Event']):
        full_count (int):
        total_pages (int):
    """

    event: List["Event"]
    full_count: int
    total_pages: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event = []
        for event_item_data in self.event:
            event_item = event_item_data.to_dict()
            event.append(event_item)

        full_count = self.full_count

        total_pages = self.total_pages

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event": event,
                "full_count": full_count,
                "total_pages": total_pages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.event import Event

        d = src_dict.copy()
        event = []
        _event = d.pop("event")
        for event_item_data in _event:
            event_item = Event.from_dict(event_item_data)

            event.append(event_item)

        full_count = d.pop("full_count")

        total_pages = d.pop("total_pages")

        event_return = cls(
            event=event,
            full_count=full_count,
            total_pages=total_pages,
        )

        event_return.additional_properties = d
        return event_return

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
