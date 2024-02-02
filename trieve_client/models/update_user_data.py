from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateUserData")


@_attrs_define
class UpdateUserData:
    """
    Attributes:
        organization_id (str): The id of the organization to update the user for.
        name (Union[None, Unset, str]): In the sense of a legal name, not a username. The new name to assign to the
            user, if not provided, the current name will be used.
        role (Union[None, Unset, int]): Either 0 (user), 1 (admin), or 2 (owner). If not provided, the current role will
            be used. The auth'ed user must have a role greater than or equal to the role being assigned.
        user_id (Union[None, Unset, str]): The id of the user to update, if not provided, the auth'ed user will be
            updated. If provided, the auth'ed user must be an admin (1) or owner (2) of the organization.
        username (Union[None, Unset, str]): The new username to assign to the user, if not provided, the current
            username will be used.
        visible_email (Union[None, Unset, bool]): Determines if the user's email is visible to other users, if not
            provided, the current value will be used.
        website (Union[None, Unset, str]): The new website to assign to the user, if not provided, the current website
            will be used. Used for linking to the user's personal or company website.
    """

    organization_id: str
    name: Union[None, Unset, str] = UNSET
    role: Union[None, Unset, int] = UNSET
    user_id: Union[None, Unset, str] = UNSET
    username: Union[None, Unset, str] = UNSET
    visible_email: Union[None, Unset, bool] = UNSET
    website: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        organization_id = self.organization_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        role: Union[None, Unset, int]
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        user_id: Union[None, Unset, str]
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        username: Union[None, Unset, str]
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        visible_email: Union[None, Unset, bool]
        if isinstance(self.visible_email, Unset):
            visible_email = UNSET
        else:
            visible_email = self.visible_email

        website: Union[None, Unset, str]
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organization_id": organization_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if role is not UNSET:
            field_dict["role"] = role
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if username is not UNSET:
            field_dict["username"] = username
        if visible_email is not UNSET:
            field_dict["visible_email"] = visible_email
        if website is not UNSET:
            field_dict["website"] = website

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        organization_id = d.pop("organization_id")

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_role(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        role = _parse_role(d.pop("role", UNSET))

        def _parse_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_username(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        username = _parse_username(d.pop("username", UNSET))

        def _parse_visible_email(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        visible_email = _parse_visible_email(d.pop("visible_email", UNSET))

        def _parse_website(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        website = _parse_website(d.pop("website", UNSET))

        update_user_data = cls(
            organization_id=organization_id,
            name=name,
            role=role,
            user_id=user_id,
            username=username,
            visible_email=visible_email,
            website=website,
        )

        update_user_data.additional_properties = d
        return update_user_data

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
