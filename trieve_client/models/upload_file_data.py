from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadFileData")


@_attrs_define
class UploadFileData:
    """
    Attributes:
        base64_file (str): Base64 encoded file. Convert + to -, / to _, and remove the ending = if present. This is the
            standard base64url encoding.
        file_mime_type (str): MIME type of the file being uploaded.
        file_name (str): Name of the file being uploaded, including the extension.
        create_chunks (Union[None, Unset, bool]): Create chunks is a boolean which determines whether or not to create
            chunks from the file. If false, you can manually chunk the file and send the chunks to the create_chunk endpoint
            with the file_id to associate chunks with the file. Meant mostly for advanced users.
        description (Union[None, Unset, str]): Description is an optional convience field so you do not have to remember
            what the file contains or is about. It will be included on the group resulting from the file which will hold its
            chunk.
        link (Union[None, Unset, str]): Link to the file. This can also be any string. This can be used to filter when
            searching for the file's resulting chunks. The link value will not affect embedding creation.
        metadata (Union[Unset, Any]): Metadata is a JSON object which can be used to filter chunks. This is useful for
            when you want to filter chunks by arbitrary metadata. Unlike with tag filtering, there is a performance hit for
            filtering on metadata. Will be passed down to the file's chunks.
        tag_set (Union[List[str], None, Unset]): Tag set is a comma separated list of tags which will be passed down to
            the chunks made from the file. Tags are used to filter chunks when searching. HNSW indices are created for each
            tag such that there is no performance loss when filtering on them.
        time_stamp (Union[None, Unset, str]): Time stamp should be an ISO 8601 combined date and time without timezone.
            Time_stamp is used for time window filtering and recency-biasing search results. Will be passed down to the
            file's chunks.
    """

    base64_file: str
    file_mime_type: str
    file_name: str
    create_chunks: Union[None, Unset, bool] = UNSET
    description: Union[None, Unset, str] = UNSET
    link: Union[None, Unset, str] = UNSET
    metadata: Union[Unset, Any] = UNSET
    tag_set: Union[List[str], None, Unset] = UNSET
    time_stamp: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        base64_file = self.base64_file

        file_mime_type = self.file_mime_type

        file_name = self.file_name

        create_chunks: Union[None, Unset, bool]
        if isinstance(self.create_chunks, Unset):
            create_chunks = UNSET
        else:
            create_chunks = self.create_chunks

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "base64_file": base64_file,
                "file_mime_type": file_mime_type,
                "file_name": file_name,
            }
        )
        if create_chunks is not UNSET:
            field_dict["create_chunks"] = create_chunks
        if description is not UNSET:
            field_dict["description"] = description
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
        base64_file = d.pop("base64_file")

        file_mime_type = d.pop("file_mime_type")

        file_name = d.pop("file_name")

        def _parse_create_chunks(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        create_chunks = _parse_create_chunks(d.pop("create_chunks", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

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

        upload_file_data = cls(
            base64_file=base64_file,
            file_mime_type=file_mime_type,
            file_name=file_name,
            create_chunks=create_chunks,
            description=description,
            link=link,
            metadata=metadata,
            tag_set=tag_set,
            time_stamp=time_stamp,
        )

        upload_file_data.additional_properties = d
        return upload_file_data

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
