import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserDTO")


@_attrs_define
class UserDTO:
    """
    Attributes:
        created_at (datetime.datetime):
        id (str):
        visible_email (bool):
        email (Union[None, Unset, str]):
        username (Union[None, Unset, str]):
        website (Union[None, Unset, str]):
    """

    created_at: datetime.datetime
    id: str
    visible_email: bool
    email: Union[None, Unset, str] = UNSET
    username: Union[None, Unset, str] = UNSET
    website: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        visible_email = self.visible_email

        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        username: Union[None, Unset, str]
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        website: Union[None, Unset, str]
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "visible_email": visible_email,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if username is not UNSET:
            field_dict["username"] = username
        if website is not UNSET:
            field_dict["website"] = website

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = isoparse(d.pop("created_at"))

        id = d.pop("id")

        visible_email = d.pop("visible_email")

        def _parse_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_username(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        username = _parse_username(d.pop("username", UNSET))

        def _parse_website(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        website = _parse_website(d.pop("website", UNSET))

        user_dto = cls(
            created_at=created_at,
            id=id,
            visible_email=visible_email,
            email=email,
            username=username,
            website=website,
        )

        user_dto.additional_properties = d
        return user_dto

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
