from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientDatasetConfiguration")


@_attrs_define
class ClientDatasetConfiguration:
    """
    Attributes:
        create_chunk_feature (Union[None, Unset, bool]):
        date_range_value (Union[None, Unset, str]):
        document_upload_feature (Union[None, Unset, bool]):
        filter_items (Union[Unset, Any]):
        frontmatter_vals (Union[None, Unset, str]):
        image_range_end_key (Union[None, Unset, str]):
        image_range_start_key (Union[None, Unset, str]):
        lines_before_show_more (Union[None, Unset, int]):
        search_queries (Union[None, Unset, str]):
        suggested_queries (Union[None, Unset, str]):
    """

    create_chunk_feature: Union[None, Unset, bool] = UNSET
    date_range_value: Union[None, Unset, str] = UNSET
    document_upload_feature: Union[None, Unset, bool] = UNSET
    filter_items: Union[Unset, Any] = UNSET
    frontmatter_vals: Union[None, Unset, str] = UNSET
    image_range_end_key: Union[None, Unset, str] = UNSET
    image_range_start_key: Union[None, Unset, str] = UNSET
    lines_before_show_more: Union[None, Unset, int] = UNSET
    search_queries: Union[None, Unset, str] = UNSET
    suggested_queries: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        create_chunk_feature: Union[None, Unset, bool]
        if isinstance(self.create_chunk_feature, Unset):
            create_chunk_feature = UNSET
        else:
            create_chunk_feature = self.create_chunk_feature

        date_range_value: Union[None, Unset, str]
        if isinstance(self.date_range_value, Unset):
            date_range_value = UNSET
        else:
            date_range_value = self.date_range_value

        document_upload_feature: Union[None, Unset, bool]
        if isinstance(self.document_upload_feature, Unset):
            document_upload_feature = UNSET
        else:
            document_upload_feature = self.document_upload_feature

        filter_items = self.filter_items

        frontmatter_vals: Union[None, Unset, str]
        if isinstance(self.frontmatter_vals, Unset):
            frontmatter_vals = UNSET
        else:
            frontmatter_vals = self.frontmatter_vals

        image_range_end_key: Union[None, Unset, str]
        if isinstance(self.image_range_end_key, Unset):
            image_range_end_key = UNSET
        else:
            image_range_end_key = self.image_range_end_key

        image_range_start_key: Union[None, Unset, str]
        if isinstance(self.image_range_start_key, Unset):
            image_range_start_key = UNSET
        else:
            image_range_start_key = self.image_range_start_key

        lines_before_show_more: Union[None, Unset, int]
        if isinstance(self.lines_before_show_more, Unset):
            lines_before_show_more = UNSET
        else:
            lines_before_show_more = self.lines_before_show_more

        search_queries: Union[None, Unset, str]
        if isinstance(self.search_queries, Unset):
            search_queries = UNSET
        else:
            search_queries = self.search_queries

        suggested_queries: Union[None, Unset, str]
        if isinstance(self.suggested_queries, Unset):
            suggested_queries = UNSET
        else:
            suggested_queries = self.suggested_queries

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if create_chunk_feature is not UNSET:
            field_dict["CREATE_CHUNK_FEATURE"] = create_chunk_feature
        if date_range_value is not UNSET:
            field_dict["DATE_RANGE_VALUE"] = date_range_value
        if document_upload_feature is not UNSET:
            field_dict["DOCUMENT_UPLOAD_FEATURE"] = document_upload_feature
        if filter_items is not UNSET:
            field_dict["FILTER_ITEMS"] = filter_items
        if frontmatter_vals is not UNSET:
            field_dict["FRONTMATTER_VALS"] = frontmatter_vals
        if image_range_end_key is not UNSET:
            field_dict["IMAGE_RANGE_END_KEY"] = image_range_end_key
        if image_range_start_key is not UNSET:
            field_dict["IMAGE_RANGE_START_KEY"] = image_range_start_key
        if lines_before_show_more is not UNSET:
            field_dict["LINES_BEFORE_SHOW_MORE"] = lines_before_show_more
        if search_queries is not UNSET:
            field_dict["SEARCH_QUERIES"] = search_queries
        if suggested_queries is not UNSET:
            field_dict["SUGGESTED_QUERIES"] = suggested_queries

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_create_chunk_feature(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        create_chunk_feature = _parse_create_chunk_feature(d.pop("CREATE_CHUNK_FEATURE", UNSET))

        def _parse_date_range_value(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        date_range_value = _parse_date_range_value(d.pop("DATE_RANGE_VALUE", UNSET))

        def _parse_document_upload_feature(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        document_upload_feature = _parse_document_upload_feature(d.pop("DOCUMENT_UPLOAD_FEATURE", UNSET))

        filter_items = d.pop("FILTER_ITEMS", UNSET)

        def _parse_frontmatter_vals(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        frontmatter_vals = _parse_frontmatter_vals(d.pop("FRONTMATTER_VALS", UNSET))

        def _parse_image_range_end_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        image_range_end_key = _parse_image_range_end_key(d.pop("IMAGE_RANGE_END_KEY", UNSET))

        def _parse_image_range_start_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        image_range_start_key = _parse_image_range_start_key(d.pop("IMAGE_RANGE_START_KEY", UNSET))

        def _parse_lines_before_show_more(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        lines_before_show_more = _parse_lines_before_show_more(d.pop("LINES_BEFORE_SHOW_MORE", UNSET))

        def _parse_search_queries(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        search_queries = _parse_search_queries(d.pop("SEARCH_QUERIES", UNSET))

        def _parse_suggested_queries(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        suggested_queries = _parse_suggested_queries(d.pop("SUGGESTED_QUERIES", UNSET))

        client_dataset_configuration = cls(
            create_chunk_feature=create_chunk_feature,
            date_range_value=date_range_value,
            document_upload_feature=document_upload_feature,
            filter_items=filter_items,
            frontmatter_vals=frontmatter_vals,
            image_range_end_key=image_range_end_key,
            image_range_start_key=image_range_start_key,
            lines_before_show_more=lines_before_show_more,
            search_queries=search_queries,
            suggested_queries=suggested_queries,
        )

        client_dataset_configuration.additional_properties = d
        return client_dataset_configuration

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
