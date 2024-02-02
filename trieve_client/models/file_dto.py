import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileDTO")


@_attrs_define
class FileDTO:
    """
    Attributes:
        created_at (datetime.datetime):
        file_name (str):
        id (str):
        s3_url (str):
        size (int):
        updated_at (datetime.datetime):
        user_id (str):
        link (Union[None, Unset, str]):
        metadata (Union[Unset, Any]):
    """

    created_at: datetime.datetime
    file_name: str
    id: str
    s3_url: str
    size: int
    updated_at: datetime.datetime
    user_id: str
    link: Union[None, Unset, str] = UNSET
    metadata: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        file_name = self.file_name

        id = self.id

        s3_url = self.s3_url

        size = self.size

        updated_at = self.updated_at.isoformat()

        user_id = self.user_id

        link: Union[None, Unset, str]
        if isinstance(self.link, Unset):
            link = UNSET
        else:
            link = self.link

        metadata = self.metadata

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "file_name": file_name,
                "id": id,
                "s3_url": s3_url,
                "size": size,
                "updated_at": updated_at,
                "user_id": user_id,
            }
        )
        if link is not UNSET:
            field_dict["link"] = link
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = isoparse(d.pop("created_at"))

        file_name = d.pop("file_name")

        id = d.pop("id")

        s3_url = d.pop("s3_url")

        size = d.pop("size")

        updated_at = isoparse(d.pop("updated_at"))

        user_id = d.pop("user_id")

        def _parse_link(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        link = _parse_link(d.pop("link", UNSET))

        metadata = d.pop("metadata", UNSET)

        file_dto = cls(
            created_at=created_at,
            file_name=file_name,
            id=id,
            s3_url=s3_url,
            size=size,
            updated_at=updated_at,
            user_id=user_id,
            link=link,
            metadata=metadata,
        )

        file_dto.additional_properties = d
        return file_dto

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
