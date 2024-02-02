from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateDatasetRequest")


@_attrs_define
class UpdateDatasetRequest:
    """
    Attributes:
        dataset_id (str): The id of the dataset you want to update.
        client_configuration (Union[Unset, Any]): The new client configuration of the dataset, can be arbitrary JSON.
            See docs.trieve.ai for more information. If not provided, the client configuration will not be updated.
        dataset_name (Union[None, Unset, str]): The new name of the dataset. Must be unique within the organization. If
            not provided, the name will not be updated.
        server_configuration (Union[Unset, Any]): The new server configuration of the dataset, can be arbitrary JSON.
            See docs.trieve.ai for more information. If not provided, the server configuration will not be updated.
    """

    dataset_id: str
    client_configuration: Union[Unset, Any] = UNSET
    dataset_name: Union[None, Unset, str] = UNSET
    server_configuration: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dataset_id = self.dataset_id

        client_configuration = self.client_configuration

        dataset_name: Union[None, Unset, str]
        if isinstance(self.dataset_name, Unset):
            dataset_name = UNSET
        else:
            dataset_name = self.dataset_name

        server_configuration = self.server_configuration

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataset_id": dataset_id,
            }
        )
        if client_configuration is not UNSET:
            field_dict["client_configuration"] = client_configuration
        if dataset_name is not UNSET:
            field_dict["dataset_name"] = dataset_name
        if server_configuration is not UNSET:
            field_dict["server_configuration"] = server_configuration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dataset_id = d.pop("dataset_id")

        client_configuration = d.pop("client_configuration", UNSET)

        def _parse_dataset_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        dataset_name = _parse_dataset_name(d.pop("dataset_name", UNSET))

        server_configuration = d.pop("server_configuration", UNSET)

        update_dataset_request = cls(
            dataset_id=dataset_id,
            client_configuration=client_configuration,
            dataset_name=dataset_name,
            server_configuration=server_configuration,
        )

        update_dataset_request.additional_properties = d
        return update_dataset_request

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
