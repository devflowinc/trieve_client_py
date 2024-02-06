from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateChunkData")


@_attrs_define
class CreateChunkData:
    """
    Attributes:
        chunk_html (Union[None, Unset, str]): HTML content of the chunk. This can also be plaintext. The innerText of
            the HTML will be used to create the embedding vector. The point of using HTML is for convienience, as some users
            have applications where users submit HTML content.
        chunk_vector (Union[List[float], None, Unset]): Chunk_vector is a vector of floats which can be used instead of
            generating a new embedding. This is useful for when you are using a pre-embedded dataset. If this is not
            provided, the innerText of the chunk_html will be used to create the embedding.
        file_id (Union[None, Unset, str]): File_uuid is the uuid of the file that the chunk is associated with. This is
            used to associate chunks with files. This is useful for when you want to delete a file and all of its associated
            chunks.
        group_ids (Union[List[str], None, Unset]): Group ids are the ids of the groups that the chunk should be placed
            into. This is useful for when you want to create a chunk and add it to a group or multiple groups in one
            request. Necessary because this route queues the chunk for ingestion and the chunk may not exist yet immediatley
            after response.
        link (Union[None, Unset, str]): Link to the chunk. This can also be any string. Frequently, this is a link to
            the source of the chunk. The link value will not affect the embedding creation.
        metadata (Union[Unset, Any]): Metadata is a JSON object which can be used to filter chunks. This is useful for
            when you want to filter chunks by arbitrary metadata. Unlike with tag filtering, there is a performance hit for
            filtering on metadata.
        tag_set (Union[List[str], None, Unset]): Tag set is a list of tags. This can be used to filter chunks by tag.
            Unlike with metadata filtering, HNSW indices will exist for each tag such that there is not a performance hit
            for filtering on them.
        time_stamp (Union[None, Unset, str]): Time_stamp should be an ISO 8601 combined date and time without timezone.
            It is used for time window filtering and recency-biasing search results.
        tracking_id (Union[None, Unset, str]): Tracking_id is a string which can be used to identify a chunk. This is
            useful for when you are coordinating with an external system and want to use the tracking_id to identify the
            chunk.
        weight (Union[None, Unset, float]): Weight is a float which can be used to bias search results. This is useful
            for when you want to bias search results for a chunk. The magnitude only matters relative to other chunks in the
            chunk's dataset dataset.
    """

    chunk_html: Union[None, Unset, str] = UNSET
    chunk_vector: Union[List[float], None, Unset] = UNSET
    file_id: Union[None, Unset, str] = UNSET
    group_ids: Union[List[str], None, Unset] = UNSET
    link: Union[None, Unset, str] = UNSET
    metadata: Union[Unset, Any] = UNSET
    tag_set: Union[List[str], None, Unset] = UNSET
    time_stamp: Union[None, Unset, str] = UNSET
    tracking_id: Union[None, Unset, str] = UNSET
    weight: Union[None, Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        chunk_html: Union[None, Unset, str]
        if isinstance(self.chunk_html, Unset):
            chunk_html = UNSET
        else:
            chunk_html = self.chunk_html

        chunk_vector: Union[List[float], None, Unset]
        if isinstance(self.chunk_vector, Unset):
            chunk_vector = UNSET
        elif isinstance(self.chunk_vector, list):
            chunk_vector = self.chunk_vector

        else:
            chunk_vector = self.chunk_vector

        file_id: Union[None, Unset, str]
        if isinstance(self.file_id, Unset):
            file_id = UNSET
        else:
            file_id = self.file_id

        group_ids: Union[List[str], None, Unset]
        if isinstance(self.group_ids, Unset):
            group_ids = UNSET
        elif isinstance(self.group_ids, list):
            group_ids = self.group_ids

        else:
            group_ids = self.group_ids

        link: Union[None, Unset, str]
        if isinstance(self.link, Unset):
            link = UNSET
        else:
            link = self.link

        metadata = self.metadata

        tag_set: Union[List[str], None, Unset]
        if isinstance(self.tag_set, Unset):
            tag_set = UNSET
        elif isinstance(self.tag_set, list):
            tag_set = self.tag_set

        else:
            tag_set = self.tag_set

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
        field_dict.update({})
        if chunk_html is not UNSET:
            field_dict["chunk_html"] = chunk_html
        if chunk_vector is not UNSET:
            field_dict["chunk_vector"] = chunk_vector
        if file_id is not UNSET:
            field_dict["file_id"] = file_id
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
        if link is not UNSET:
            field_dict["link"] = link
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if tag_set is not UNSET:
            field_dict["tag_set"] = tag_set
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

        def _parse_chunk_html(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        chunk_html = _parse_chunk_html(d.pop("chunk_html", UNSET))

        def _parse_chunk_vector(data: object) -> Union[List[float], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                chunk_vector_type_0 = cast(List[float], data)

                return chunk_vector_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[float], None, Unset], data)

        chunk_vector = _parse_chunk_vector(d.pop("chunk_vector", UNSET))

        def _parse_file_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        file_id = _parse_file_id(d.pop("file_id", UNSET))

        def _parse_group_ids(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                group_ids_type_0 = cast(List[str], data)

                return group_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        group_ids = _parse_group_ids(d.pop("group_ids", UNSET))

        def _parse_link(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        link = _parse_link(d.pop("link", UNSET))

        metadata = d.pop("metadata", UNSET)

        def _parse_tag_set(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tag_set_type_0 = cast(List[str], data)

                return tag_set_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        tag_set = _parse_tag_set(d.pop("tag_set", UNSET))

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

        create_chunk_data = cls(
            chunk_html=chunk_html,
            chunk_vector=chunk_vector,
            file_id=file_id,
            group_ids=group_ids,
            link=link,
            metadata=metadata,
            tag_set=tag_set,
            time_stamp=time_stamp,
            tracking_id=tracking_id,
            weight=weight,
        )

        create_chunk_data.additional_properties = d
        return create_chunk_data

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
