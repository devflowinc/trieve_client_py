from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTopicData")


@_attrs_define
class CreateTopicData:
    """
    Attributes:
        first_user_message (Union[None, Unset, str]): The first message which will belong to the topic. The topic name
            is generated based on this message similar to how it works in the OpenAI chat UX if a name is not explicitly
            provided on the name request body key.
        model (Union[None, Unset, str]): The model to use for the assistant's messages. This can be any model from the
            openrouter model list. If no model is provided, the gryphe/mythomax-l2-13b will be used.
        name (Union[None, Unset, str]): The name of the topic. If this is not provided, the topic name is generated from
            the first_user_message.
    """

    first_user_message: Union[None, Unset, str] = UNSET
    model: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        first_user_message: Union[None, Unset, str]
        if isinstance(self.first_user_message, Unset):
            first_user_message = UNSET
        else:
            first_user_message = self.first_user_message

        model: Union[None, Unset, str]
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_user_message is not UNSET:
            field_dict["first_user_message"] = first_user_message
        if model is not UNSET:
            field_dict["model"] = model
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_first_user_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        first_user_message = _parse_first_user_message(d.pop("first_user_message", UNSET))

        def _parse_model(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        model = _parse_model(d.pop("model", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        create_topic_data = cls(
            first_user_message=first_user_message,
            model=model,
            name=name,
        )

        create_topic_data.additional_properties = d
        return create_topic_data

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
