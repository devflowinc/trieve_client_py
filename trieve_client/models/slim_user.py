from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization import Organization
    from ..models.user_organization import UserOrganization


T = TypeVar("T", bound="SlimUser")


@_attrs_define
class SlimUser:
    """
    Attributes:
        email (str):
        id (str):
        orgs (List['Organization']):
        user_orgs (List['UserOrganization']):
        visible_email (bool):
        name (Union[None, Unset, str]):
        username (Union[None, Unset, str]):
        website (Union[None, Unset, str]):
    """

    email: str
    id: str
    orgs: List["Organization"]
    user_orgs: List["UserOrganization"]
    visible_email: bool
    name: Union[None, Unset, str] = UNSET
    username: Union[None, Unset, str] = UNSET
    website: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email

        id = self.id

        orgs = []
        for orgs_item_data in self.orgs:
            orgs_item = orgs_item_data.to_dict()
            orgs.append(orgs_item)

        user_orgs = []
        for user_orgs_item_data in self.user_orgs:
            user_orgs_item = user_orgs_item_data.to_dict()
            user_orgs.append(user_orgs_item)

        visible_email = self.visible_email

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

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
                "email": email,
                "id": id,
                "orgs": orgs,
                "user_orgs": user_orgs,
                "visible_email": visible_email,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if username is not UNSET:
            field_dict["username"] = username
        if website is not UNSET:
            field_dict["website"] = website

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.organization import Organization
        from ..models.user_organization import UserOrganization

        d = src_dict.copy()
        email = d.pop("email")

        id = d.pop("id")

        orgs = []
        _orgs = d.pop("orgs")
        for orgs_item_data in _orgs:
            orgs_item = Organization.from_dict(orgs_item_data)

            orgs.append(orgs_item)

        user_orgs = []
        _user_orgs = d.pop("user_orgs")
        for user_orgs_item_data in _user_orgs:
            user_orgs_item = UserOrganization.from_dict(user_orgs_item_data)

            user_orgs.append(user_orgs_item)

        visible_email = d.pop("visible_email")

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

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

        slim_user = cls(
            email=email,
            id=id,
            orgs=orgs,
            user_orgs=user_orgs,
            visible_email=visible_email,
            name=name,
            username=username,
            website=website,
        )

        slim_user.additional_properties = d
        return slim_user

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
