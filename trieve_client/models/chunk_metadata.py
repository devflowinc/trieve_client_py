import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChunkMetadata")


@_attrs_define
class ChunkMetadata:
    """
    Attributes:
        content (str):
        created_at (datetime.datetime):
        dataset_id (str):
        id (str):
        updated_at (datetime.datetime):
        weight (float):
        chunk_html (Union[None, Unset, str]):
        link (Union[None, Unset, str]):
        metadata (Union[Unset, Any]):
        qdrant_point_id (Union[None, Unset, str]):
        tag_set (Union[None, Unset, str]):
        time_stamp (Union[None, Unset, datetime.datetime]):
        tracking_id (Union[None, Unset, str]):
    """

    content: str
    created_at: datetime.datetime
    dataset_id: str
    id: str
    updated_at: datetime.datetime
    weight: float
    chunk_html: Union[None, Unset, str] = UNSET
    link: Union[None, Unset, str] = UNSET
    metadata: Union[Unset, Any] = UNSET
    qdrant_point_id: Union[None, Unset, str] = UNSET
    tag_set: Union[None, Unset, str] = UNSET
    time_stamp: Union[None, Unset, datetime.datetime] = UNSET
    tracking_id: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content = self.content

        created_at = self.created_at.isoformat()

        dataset_id = self.dataset_id

        id = self.id

        updated_at = self.updated_at.isoformat()

        weight = self.weight

        chunk_html: Union[None, Unset, str]
        if isinstance(self.chunk_html, Unset):
            chunk_html = UNSET
        else:
            chunk_html = self.chunk_html

        link: Union[None, Unset, str]
        if isinstance(self.link, Unset):
            link = UNSET
        else:
            link = self.link

        metadata = self.metadata

        qdrant_point_id: Union[None, Unset, str]
        if isinstance(self.qdrant_point_id, Unset):
            qdrant_point_id = UNSET
        else:
            qdrant_point_id = self.qdrant_point_id

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

        tracking_id: Union[None, Unset, str]
        if isinstance(self.tracking_id, Unset):
            tracking_id = UNSET
        else:
            tracking_id = self.tracking_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "created_at": created_at,
                "dataset_id": dataset_id,
                "id": id,
                "updated_at": updated_at,
                "weight": weight,
            }
        )
        if chunk_html is not UNSET:
            field_dict["chunk_html"] = chunk_html
        if link is not UNSET:
            field_dict["link"] = link
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if qdrant_point_id is not UNSET:
            field_dict["qdrant_point_id"] = qdrant_point_id
        if tag_set is not UNSET:
            field_dict["tag_set"] = tag_set
        if time_stamp is not UNSET:
            field_dict["time_stamp"] = time_stamp
        if tracking_id is not UNSET:
            field_dict["tracking_id"] = tracking_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content = d.pop("content")

        created_at = isoparse(d.pop("created_at"))

        dataset_id = d.pop("dataset_id")

        id = d.pop("id")

        updated_at = isoparse(d.pop("updated_at"))

        weight = d.pop("weight")

        def _parse_chunk_html(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        chunk_html = _parse_chunk_html(d.pop("chunk_html", UNSET))

        def _parse_link(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        link = _parse_link(d.pop("link", UNSET))

        metadata = d.pop("metadata", UNSET)

        def _parse_qdrant_point_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        qdrant_point_id = _parse_qdrant_point_id(d.pop("qdrant_point_id", UNSET))

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

        def _parse_tracking_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tracking_id = _parse_tracking_id(d.pop("tracking_id", UNSET))

        chunk_metadata = cls(
            content=content,
            created_at=created_at,
            dataset_id=dataset_id,
            id=id,
            updated_at=updated_at,
            weight=weight,
            chunk_html=chunk_html,
            link=link,
            metadata=metadata,
            qdrant_point_id=qdrant_point_id,
            tag_set=tag_set,
            time_stamp=time_stamp,
            tracking_id=tracking_id,
        )

        chunk_metadata.additional_properties = d
        return chunk_metadata

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
