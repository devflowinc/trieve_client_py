from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchGroupsData")


@_attrs_define
class SearchGroupsData:
    """
    Attributes:
        group_id (str): Group specifies the group to search within. Results will only consist of chunks which are
            bookmarks within the specified group.
        query (str): The query is the search query. This can be any string. The query will be used to create an
            embedding vector and/or SPLADE vector which will be used to find the result set.
        search_type (str): Search_type can be either "semantic", "fulltext", or "hybrid". "hybrid" will pull in one page
            (10 chunks) of both semantic and full-text results then re-rank them using BAAI/bge-reranker-large. "semantic"
            will pull in one page (10 chunks) of the nearest cosine distant vectors. "fulltext" will pull in one page (10
            chunks) of full-text results based on SPLADE.
        date_bias (Union[None, Unset, bool]): Set date_bias to true to bias search results towards more recent chunks.
            This will work best in hybrid search mode.
        filters (Union[Unset, Any]): Filters is a JSON object which can be used to filter chunks. The values on each key
            in the object will be used to check for an exact substring match on the metadata values for each existing chunk.
            This is useful for when you want to filter chunks by arbitrary metadata. Unlike with tag filtering, there is a
            performance hit for filtering on metadata.
        highlight_delimiters (Union[List[str], None, Unset]): Set highlight_delimiters to a list of strings to use as
            delimiters for highlighting.
        highlight_results (Union[None, Unset, bool]): Set highlight_results to true to highlight the results.
        link (Union[List[str], None, Unset]): The link set is a list of links. This can be used to filter chunks by
            link. HNSW indices do not exist for links, so there is a performance hit for filtering on them.
        page (Union[None, Unset, int]): The page of chunks to fetch. Each page is 10 chunks. Support for custom page
            size is coming soon.
        tag_set (Union[List[str], None, Unset]): The tag set is a list of tags. This can be used to filter chunks by
            tag. Unlike with metadata filtering, HNSW indices will exist for each tag such that there is not a performance
            hit for filtering on them.
    """

    group_id: str
    query: str
    search_type: str
    date_bias: Union[None, Unset, bool] = UNSET
    filters: Union[Unset, Any] = UNSET
    highlight_delimiters: Union[List[str], None, Unset] = UNSET
    highlight_results: Union[None, Unset, bool] = UNSET
    link: Union[List[str], None, Unset] = UNSET
    page: Union[None, Unset, int] = UNSET
    tag_set: Union[List[str], None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group_id = self.group_id

        query = self.query

        search_type = self.search_type

        date_bias: Union[None, Unset, bool]
        if isinstance(self.date_bias, Unset):
            date_bias = UNSET
        else:
            date_bias = self.date_bias

        filters = self.filters

        highlight_delimiters: Union[List[str], None, Unset]
        if isinstance(self.highlight_delimiters, Unset):
            highlight_delimiters = UNSET
        elif isinstance(self.highlight_delimiters, list):
            highlight_delimiters = self.highlight_delimiters

        else:
            highlight_delimiters = self.highlight_delimiters

        highlight_results: Union[None, Unset, bool]
        if isinstance(self.highlight_results, Unset):
            highlight_results = UNSET
        else:
            highlight_results = self.highlight_results

        link: Union[List[str], None, Unset]
        if isinstance(self.link, Unset):
            link = UNSET
        elif isinstance(self.link, list):
            link = self.link

        else:
            link = self.link

        page: Union[None, Unset, int]
        if isinstance(self.page, Unset):
            page = UNSET
        else:
            page = self.page

        tag_set: Union[List[str], None, Unset]
        if isinstance(self.tag_set, Unset):
            tag_set = UNSET
        elif isinstance(self.tag_set, list):
            tag_set = self.tag_set

        else:
            tag_set = self.tag_set

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "group_id": group_id,
                "query": query,
                "search_type": search_type,
            }
        )
        if date_bias is not UNSET:
            field_dict["date_bias"] = date_bias
        if filters is not UNSET:
            field_dict["filters"] = filters
        if highlight_delimiters is not UNSET:
            field_dict["highlight_delimiters"] = highlight_delimiters
        if highlight_results is not UNSET:
            field_dict["highlight_results"] = highlight_results
        if link is not UNSET:
            field_dict["link"] = link
        if page is not UNSET:
            field_dict["page"] = page
        if tag_set is not UNSET:
            field_dict["tag_set"] = tag_set

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        group_id = d.pop("group_id")

        query = d.pop("query")

        search_type = d.pop("search_type")

        def _parse_date_bias(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        date_bias = _parse_date_bias(d.pop("date_bias", UNSET))

        filters = d.pop("filters", UNSET)

        def _parse_highlight_delimiters(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                highlight_delimiters_type_0 = cast(List[str], data)

                return highlight_delimiters_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        highlight_delimiters = _parse_highlight_delimiters(d.pop("highlight_delimiters", UNSET))

        def _parse_highlight_results(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        highlight_results = _parse_highlight_results(d.pop("highlight_results", UNSET))

        def _parse_link(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                link_type_0 = cast(List[str], data)

                return link_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        link = _parse_link(d.pop("link", UNSET))

        def _parse_page(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        page = _parse_page(d.pop("page", UNSET))

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

        search_groups_data = cls(
            group_id=group_id,
            query=query,
            search_type=search_type,
            date_bias=date_bias,
            filters=filters,
            highlight_delimiters=highlight_delimiters,
            highlight_results=highlight_results,
            link=link,
            page=page,
            tag_set=tag_set,
        )

        search_groups_data.additional_properties = d
        return search_groups_data

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
