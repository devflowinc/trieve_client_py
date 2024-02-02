from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InvitationData")


@_attrs_define
class InvitationData:
    """
    Attributes:
        app_url (str): The url of the app that the user will be directed to in order to set their password. Usually
            admin.trieve.ai, but may differ for local dev or self-hosted setups.
        email (str): The email of the user to invite. Must be a valid email as they will be sent an email to register.
        organization_id (str): The id of the organization to invite the user to.
        redirect_uri (str): The url that the user will be redirected to after setting their password.
        user_role (int): The role the user will have in the organization. 0 = User, 1 = Admin, 2 = Owner.
    """

    app_url: str
    email: str
    organization_id: str
    redirect_uri: str
    user_role: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        app_url = self.app_url

        email = self.email

        organization_id = self.organization_id

        redirect_uri = self.redirect_uri

        user_role = self.user_role

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app_url": app_url,
                "email": email,
                "organization_id": organization_id,
                "redirect_uri": redirect_uri,
                "user_role": user_role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        app_url = d.pop("app_url")

        email = d.pop("email")

        organization_id = d.pop("organization_id")

        redirect_uri = d.pop("redirect_uri")

        user_role = d.pop("user_role")

        invitation_data = cls(
            app_url=app_url,
            email=email,
            organization_id=organization_id,
            redirect_uri=redirect_uri,
            user_role=user_role,
        )

        invitation_data.additional_properties = d
        return invitation_data

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
