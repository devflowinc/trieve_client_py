from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthQuery")


@_attrs_define
class AuthQuery:
    """
    Attributes:
        inv_code (Union[None, Unset, str]): Code sent via email as a result of successful call to send_invitation
        organization_id (Union[None, Unset, str]): ID of organization to authenticate into
        redirect_uri (Union[None, Unset, str]): URL to redirect to after successful login
    """

    inv_code: Union[None, Unset, str] = UNSET
    organization_id: Union[None, Unset, str] = UNSET
    redirect_uri: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        inv_code: Union[None, Unset, str]
        if isinstance(self.inv_code, Unset):
            inv_code = UNSET
        else:
            inv_code = self.inv_code

        organization_id: Union[None, Unset, str]
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        else:
            organization_id = self.organization_id

        redirect_uri: Union[None, Unset, str]
        if isinstance(self.redirect_uri, Unset):
            redirect_uri = UNSET
        else:
            redirect_uri = self.redirect_uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inv_code is not UNSET:
            field_dict["inv_code"] = inv_code
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if redirect_uri is not UNSET:
            field_dict["redirect_uri"] = redirect_uri

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_inv_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        inv_code = _parse_inv_code(d.pop("inv_code", UNSET))

        def _parse_organization_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        organization_id = _parse_organization_id(d.pop("organization_id", UNSET))

        def _parse_redirect_uri(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        redirect_uri = _parse_redirect_uri(d.pop("redirect_uri", UNSET))

        auth_query = cls(
            inv_code=inv_code,
            organization_id=organization_id,
            redirect_uri=redirect_uri,
        )

        auth_query.additional_properties = d
        return auth_query

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
