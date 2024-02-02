from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteGroupData")


@_attrs_define
class DeleteGroupData:
    """
    Attributes:
        delete_chunks (Union[None, Unset, bool]):
    """

    delete_chunks: Union[None, Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        delete_chunks: Union[None, Unset, bool]
        if isinstance(self.delete_chunks, Unset):
            delete_chunks = UNSET
        else:
            delete_chunks = self.delete_chunks

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delete_chunks is not UNSET:
            field_dict["delete_chunks"] = delete_chunks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_delete_chunks(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        delete_chunks = _parse_delete_chunks(d.pop("delete_chunks", UNSET))

        delete_group_data = cls(
            delete_chunks=delete_chunks,
        )

        delete_group_data.additional_properties = d
        return delete_group_data

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
