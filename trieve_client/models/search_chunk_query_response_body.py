from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.score_chunk_dto import ScoreChunkDTO


T = TypeVar("T", bound="SearchChunkQueryResponseBody")


@_attrs_define
class SearchChunkQueryResponseBody:
    """
    Attributes:
        score_chunks (List['ScoreChunkDTO']):
        total_chunk_pages (int):
    """

    score_chunks: List["ScoreChunkDTO"]
    total_chunk_pages: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        score_chunks = []
        for score_chunks_item_data in self.score_chunks:
            score_chunks_item = score_chunks_item_data.to_dict()
            score_chunks.append(score_chunks_item)

        total_chunk_pages = self.total_chunk_pages

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "score_chunks": score_chunks,
                "total_chunk_pages": total_chunk_pages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.score_chunk_dto import ScoreChunkDTO

        d = src_dict.copy()
        score_chunks = []
        _score_chunks = d.pop("score_chunks")
        for score_chunks_item_data in _score_chunks:
            score_chunks_item = ScoreChunkDTO.from_dict(score_chunks_item_data)

            score_chunks.append(score_chunks_item)

        total_chunk_pages = d.pop("total_chunk_pages")

        search_chunk_query_response_body = cls(
            score_chunks=score_chunks,
            total_chunk_pages=total_chunk_pages,
        )

        search_chunk_query_response_body.additional_properties = d
        return search_chunk_query_response_body

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
