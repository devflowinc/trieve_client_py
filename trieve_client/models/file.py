import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="File")


@_attrs_define
class File:
    """
    Attributes:
        created_at (datetime.datetime):
        dataset_id (str):
        file_name (str):
        id (str):
        size (int):
        updated_at (datetime.datetime):
        user_id (str):
        link (Union[None, Unset, str]):
        metadata (Union[Unset, Any]):
        tag_set (Union[None, Unset, str]):
        time_stamp (Union[None, Unset, datetime.datetime]):
    """

    created_at: datetime.datetime
    dataset_id: str
    file_name: str
    id: str
    size: int
    updated_at: datetime.datetime
    user_id: str
    link: Union[None, Unset, str] = UNSET
    metadata: Union[Unset, Any] = UNSET
    tag_set: Union[None, Unset, str] = UNSET
    time_stamp: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        dataset_id = self.dataset_id

        file_name = self.file_name

        id = self.id

        size = self.size

        updated_at = self.updated_at.isoformat()

        user_id = self.user_id

        link: Union[None, Unset, str]
        if isinstance(self.link, Unset):
            link = UNSET
        else:
            link = self.link

        metadata = self.metadata

        tag_set: Union[None, Unset, str]
        if isinstance(self.tag_set, Unset):
            tag_set = UNSET
        else:
            tag_set = self.tag_set

        time_stamp: Union[None, Unset, str]
        if isinstance(self.time_stamp, Unset):
            time_stamp = UNSET
        elif isinstance(self.time_stamp, datetime.datetime):
            time_stamp = self.time_stamp.isoformat()
        else:
            time_stamp = self.time_stamp

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "dataset_id": dataset_id,
                "file_name": file_name,
                "id": id,
                "size": size,
                "updated_at": updated_at,
                "user_id": user_id,
            }
        )
        if link is not UNSET:
            field_dict["link"] = link
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if tag_set is not UNSET:
            field_dict["tag_set"] = tag_set
        if time_stamp is not UNSET:
            field_dict["time_stamp"] = time_stamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = isoparse(d.pop("created_at"))

        dataset_id = d.pop("dataset_id")

        file_name = d.pop("file_name")

        id = d.pop("id")

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

        def _parse_tag_set(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tag_set = _parse_tag_set(d.pop("tag_set", UNSET))

        def _parse_time_stamp(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                time_stamp_type_0 = isoparse(data)

                return time_stamp_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        time_stamp = _parse_time_stamp(d.pop("time_stamp", UNSET))

        file = cls(
            created_at=created_at,
            dataset_id=dataset_id,
            file_name=file_name,
            id=id,
            size=size,
            updated_at=updated_at,
            user_id=user_id,
            link=link,
            metadata=metadata,
            tag_set=tag_set,
            time_stamp=time_stamp,
        )

        file.additional_properties = d
        return file

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
