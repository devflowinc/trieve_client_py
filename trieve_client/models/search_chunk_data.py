from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_chunk_data_time_range_type_0_item import SearchChunkDataTimeRangeType0Item
    from ..models.search_chunk_data_weights_type_0_item import SearchChunkDataWeightsType0Item


T = TypeVar("T", bound="SearchChunkData")


@_attrs_define
class SearchChunkData:
    """
    Attributes:
        query (str): Query is the search query. This can be any string. The query will be used to create an embedding
            vector and/or SPLADE vector which will be used to find the result set.
        search_type (str): Can be either "semantic", "fulltext", or "hybrid". "hybrid" will pull in one page (10 chunks)
            of both semantic and full-text results then re-rank them using reciprocal rank fusion using the specified
            weights or BAAI/bge-reranker-large. "semantic" will pull in one page (10 chunks) of the nearest cosine distant
            vectors. "fulltext" will pull in one page (10 chunks) of full-text results based on SPLADE.
        cross_encoder (Union[None, Unset, bool]): Set cross_encoder to true to use the BAAI/bge-reranker-large model to
            re-rank search results. This will only apply if in hybrid search mode. Reciprocal rank fusion will be used if
            cross_encoder is set to false or not set.
        date_bias (Union[None, Unset, bool]): Set date_bias to true to bias search results towards more recent chunks.
            This will work best in hybrid search mode.
        filters (Union[Unset, Any]): Filters is a JSON object which can be used to filter chunks. The values on each key
            in the object will be used to check for an exact substring match on the metadata values for each existing chunk.
            This is useful for when you want to filter chunks by arbitrary metadata. Unlike with tag filtering, there is a
            performance hit for filtering on metadata.
        get_collisions (Union[None, Unset, bool]): Set get_collisions to true to get the collisions for each chunk. This
            will only apply if
            environment variable COLLISIONS_ENABLED is set to true.
        highlight_delimiters (Union[List[str], None, Unset]): Set highlight_delimiters to a list of strings to use as
            delimiters for highlighting.
        highlight_results (Union[None, Unset, bool]): Set highlight_results to true to highlight the results.
        link (Union[List[str], None, Unset]): Link set is a comma separated list of links. This can be used to filter
            chunks by link. HNSW indices do not exist for links, so there is a performance hit for filtering on them.
        page (Union[None, Unset, int]): Page of chunks to fetch. Each page is 10 chunks. Support for custom page size is
            coming soon.
        tag_set (Union[List[str], None, Unset]): Tag_set is a comma separated list of tags. This can be used to filter
            chunks by tag. Unlike with metadata filtering, HNSW indices will exist for each tag such that there is not a
            performance hit for filtering on them.
        time_range (Union[List['SearchChunkDataTimeRangeType0Item'], None, Unset]): Time_range is a tuple of two ISO
            8601 combined date and time without timezone. The first value is the start of the time range and the second
            value is the end of the time range. This can be used to filter chunks by time range. HNSW indices do not exist
            for time range, so there is a performance hit for filtering on them.
        weights (Union[List['SearchChunkDataWeightsType0Item'], None, Unset]): Weights are a tuple of two floats. The
            first value is the weight for the semantic search results and the second value is the weight for the full-text
            search results. This can be used to bias search results towards semantic or full-text results. This will only
            apply if in hybrid search mode and cross_encoder is set to false.
    """

    query: str
    search_type: str
    cross_encoder: Union[None, Unset, bool] = UNSET
    date_bias: Union[None, Unset, bool] = UNSET
    filters: Union[Unset, Any] = UNSET
    get_collisions: Union[None, Unset, bool] = UNSET
    highlight_delimiters: Union[List[str], None, Unset] = UNSET
    highlight_results: Union[None, Unset, bool] = UNSET
    link: Union[List[str], None, Unset] = UNSET
    page: Union[None, Unset, int] = UNSET
    tag_set: Union[List[str], None, Unset] = UNSET
    time_range: Union[List["SearchChunkDataTimeRangeType0Item"], None, Unset] = UNSET
    weights: Union[List["SearchChunkDataWeightsType0Item"], None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query = self.query

        search_type = self.search_type

        cross_encoder: Union[None, Unset, bool]
        if isinstance(self.cross_encoder, Unset):
            cross_encoder = UNSET
        else:
            cross_encoder = self.cross_encoder

        date_bias: Union[None, Unset, bool]
        if isinstance(self.date_bias, Unset):
            date_bias = UNSET
        else:
            date_bias = self.date_bias

        filters = self.filters

        get_collisions: Union[None, Unset, bool]
        if isinstance(self.get_collisions, Unset):
            get_collisions = UNSET
        else:
            get_collisions = self.get_collisions

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

        time_range: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.time_range, Unset):
            time_range = UNSET
        elif isinstance(self.time_range, list):
            time_range = []
            for time_range_type_0_item_data in self.time_range:
                time_range_type_0_item = time_range_type_0_item_data.to_dict()
                time_range.append(time_range_type_0_item)

        else:
            time_range = self.time_range

        weights: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.weights, Unset):
            weights = UNSET
        elif isinstance(self.weights, list):
            weights = []
            for weights_type_0_item_data in self.weights:
                weights_type_0_item = weights_type_0_item_data.to_dict()
                weights.append(weights_type_0_item)

        else:
            weights = self.weights

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
                "search_type": search_type,
            }
        )
        if cross_encoder is not UNSET:
            field_dict["cross_encoder"] = cross_encoder
        if date_bias is not UNSET:
            field_dict["date_bias"] = date_bias
        if filters is not UNSET:
            field_dict["filters"] = filters
        if get_collisions is not UNSET:
            field_dict["get_collisions"] = get_collisions
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
        if time_range is not UNSET:
            field_dict["time_range"] = time_range
        if weights is not UNSET:
            field_dict["weights"] = weights

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.search_chunk_data_time_range_type_0_item import SearchChunkDataTimeRangeType0Item
        from ..models.search_chunk_data_weights_type_0_item import SearchChunkDataWeightsType0Item

        d = src_dict.copy()
        query = d.pop("query")

        search_type = d.pop("search_type")

        def _parse_cross_encoder(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        cross_encoder = _parse_cross_encoder(d.pop("cross_encoder", UNSET))

        def _parse_date_bias(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        date_bias = _parse_date_bias(d.pop("date_bias", UNSET))

        filters = d.pop("filters", UNSET)

        def _parse_get_collisions(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        get_collisions = _parse_get_collisions(d.pop("get_collisions", UNSET))

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

        def _parse_time_range(data: object) -> Union[List["SearchChunkDataTimeRangeType0Item"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                time_range_type_0 = []
                _time_range_type_0 = data
                for time_range_type_0_item_data in _time_range_type_0:
                    time_range_type_0_item = SearchChunkDataTimeRangeType0Item.from_dict(time_range_type_0_item_data)

                    time_range_type_0.append(time_range_type_0_item)

                return time_range_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["SearchChunkDataTimeRangeType0Item"], None, Unset], data)

        time_range = _parse_time_range(d.pop("time_range", UNSET))

        def _parse_weights(data: object) -> Union[List["SearchChunkDataWeightsType0Item"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                weights_type_0 = []
                _weights_type_0 = data
                for weights_type_0_item_data in _weights_type_0:
                    weights_type_0_item = SearchChunkDataWeightsType0Item.from_dict(weights_type_0_item_data)

                    weights_type_0.append(weights_type_0_item)

                return weights_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["SearchChunkDataWeightsType0Item"], None, Unset], data)

        weights = _parse_weights(d.pop("weights", UNSET))

        search_chunk_data = cls(
            query=query,
            search_type=search_type,
            cross_encoder=cross_encoder,
            date_bias=date_bias,
            filters=filters,
            get_collisions=get_collisions,
            highlight_delimiters=highlight_delimiters,
            highlight_results=highlight_results,
            link=link,
            page=page,
            tag_set=tag_set,
            time_range=time_range,
            weights=weights,
        )

        search_chunk_data.additional_properties = d
        return search_chunk_data

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
