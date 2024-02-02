from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateChunkData")


@_attrs_define
class UpdateChunkData:
    """
    Attributes:
        chunk_uuid (str): Id of the chunk you want to update.
        chunk_html (Union[None, Unset, str]): HTML content of the chunk you want to update. This can also be plaintext.
            The innerText of the HTML will be used to create the embedding vector. The point of using HTML is for
            convienience, as some users have applications where users submit HTML content. If no chunk_html is provided, the
            existing chunk_html will be used.
        link (Union[None, Unset, str]): Link of the chunk you want to update. This can also be any string. Frequently,
            this is a link to the source of the chunk. The link value will not affect the embedding creation. If no link is
            provided, the existing link will be used.
        metadata (Union[Unset, Any]): The metadata is a JSON object which can be used to filter chunks. This is useful
            for when you want to filter chunks by arbitrary metadata. Unlike with tag filtering, there is a performance hit
            for filtering on metadata. If no metadata is provided, the existing metadata will be used.
        time_stamp (Union[None, Unset, str]): Time_stamp should be an ISO 8601 combined date and time without timezone.
            It is used for time window filtering and recency-biasing search results. If no time_stamp is provided, the
            existing time_stamp will be used.
        tracking_id (Union[None, Unset, str]): Tracking_id is a string which can be used to identify a chunk. This is
            useful for when you are coordinating with an external system and want to use the tracking_id to identify the
            chunk. If no tracking_id is provided, the existing tracking_id will be used.
        weight (Union[None, Unset, float]): Weight is a float which can be used to bias search results. This is useful
            for when you want to bias search results for a chunk. The magnitude only matters relative to other chunks in the
            chunk's dataset dataset. If no weight is provided, the existing weight will be used.
    """

    chunk_uuid: str
    chunk_html: Union[None, Unset, str] = UNSET
    link: Union[None, Unset, str] = UNSET
    metadata: Union[Unset, Any] = UNSET
    time_stamp: Union[None, Unset, str] = UNSET
    tracking_id: Union[None, Unset, str] = UNSET
    weight: Union[None, Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        chunk_uuid = self.chunk_uuid

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

        time_stamp: Union[None, Unset, str]
        if isinstance(self.time_stamp, Unset):
            time_stamp = UNSET
        else:
            time_stamp = self.time_stamp

        tracking_id: Union[None, Unset, str]
        if isinstance(self.tracking_id, Unset):
            tracking_id = UNSET
        else:
            tracking_id = self.tracking_id

        weight: Union[None, Unset, float]
        if isinstance(self.weight, Unset):
            weight = UNSET
        else:
            weight = self.weight

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chunk_uuid": chunk_uuid,
            }
        )
        if chunk_html is not UNSET:
            field_dict["chunk_html"] = chunk_html
        if link is not UNSET:
            field_dict["link"] = link
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if time_stamp is not UNSET:
            field_dict["time_stamp"] = time_stamp
        if tracking_id is not UNSET:
            field_dict["tracking_id"] = tracking_id
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        chunk_uuid = d.pop("chunk_uuid")

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

        def _parse_time_stamp(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        time_stamp = _parse_time_stamp(d.pop("time_stamp", UNSET))

        def _parse_tracking_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tracking_id = _parse_tracking_id(d.pop("tracking_id", UNSET))

        def _parse_weight(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        weight = _parse_weight(d.pop("weight", UNSET))

        update_chunk_data = cls(
            chunk_uuid=chunk_uuid,
            chunk_html=chunk_html,
            link=link,
            metadata=metadata,
            time_stamp=time_stamp,
            tracking_id=tracking_id,
            weight=weight,
        )

        update_chunk_data.additional_properties = d
        return update_chunk_data

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
