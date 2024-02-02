import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Message")


@_attrs_define
class Message:
    """
    Attributes:
        content (str):
        created_at (datetime.datetime):
        dataset_id (str):
        deleted (bool):
        id (str):
        role (str):
        sort_order (int):
        topic_id (str):
        updated_at (datetime.datetime):
        completion_tokens (Union[None, Unset, int]):
        prompt_tokens (Union[None, Unset, int]):
    """

    content: str
    created_at: datetime.datetime
    dataset_id: str
    deleted: bool
    id: str
    role: str
    sort_order: int
    topic_id: str
    updated_at: datetime.datetime
    completion_tokens: Union[None, Unset, int] = UNSET
    prompt_tokens: Union[None, Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content = self.content

        created_at = self.created_at.isoformat()

        dataset_id = self.dataset_id

        deleted = self.deleted

        id = self.id

        role = self.role

        sort_order = self.sort_order

        topic_id = self.topic_id

        updated_at = self.updated_at.isoformat()

        completion_tokens: Union[None, Unset, int]
        if isinstance(self.completion_tokens, Unset):
            completion_tokens = UNSET
        else:
            completion_tokens = self.completion_tokens

        prompt_tokens: Union[None, Unset, int]
        if isinstance(self.prompt_tokens, Unset):
            prompt_tokens = UNSET
        else:
            prompt_tokens = self.prompt_tokens

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "created_at": created_at,
                "dataset_id": dataset_id,
                "deleted": deleted,
                "id": id,
                "role": role,
                "sort_order": sort_order,
                "topic_id": topic_id,
                "updated_at": updated_at,
            }
        )
        if completion_tokens is not UNSET:
            field_dict["completion_tokens"] = completion_tokens
        if prompt_tokens is not UNSET:
            field_dict["prompt_tokens"] = prompt_tokens

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content = d.pop("content")

        created_at = isoparse(d.pop("created_at"))

        dataset_id = d.pop("dataset_id")

        deleted = d.pop("deleted")

        id = d.pop("id")

        role = d.pop("role")

        sort_order = d.pop("sort_order")

        topic_id = d.pop("topic_id")

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_completion_tokens(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        completion_tokens = _parse_completion_tokens(d.pop("completion_tokens", UNSET))

        def _parse_prompt_tokens(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        prompt_tokens = _parse_prompt_tokens(d.pop("prompt_tokens", UNSET))

        message = cls(
            content=content,
            created_at=created_at,
            dataset_id=dataset_id,
            deleted=deleted,
            id=id,
            role=role,
            sort_order=sort_order,
            topic_id=topic_id,
            updated_at=updated_at,
            completion_tokens=completion_tokens,
            prompt_tokens=prompt_tokens,
        )

        message.additional_properties = d
        return message

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
