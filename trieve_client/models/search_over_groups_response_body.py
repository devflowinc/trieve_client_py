from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.group_score_chunk_dto import GroupScoreChunkDTO


T = TypeVar("T", bound="SearchOverGroupsResponseBody")


@_attrs_define
class SearchOverGroupsResponseBody:
    """
    Attributes:
        group_chunks (List['GroupScoreChunkDTO']):
        total_chunk_pages (int):
    """

    group_chunks: List["GroupScoreChunkDTO"]
    total_chunk_pages: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group_chunks = []
        for group_chunks_item_data in self.group_chunks:
            group_chunks_item = group_chunks_item_data.to_dict()
            group_chunks.append(group_chunks_item)

        total_chunk_pages = self.total_chunk_pages

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "group_chunks": group_chunks,
                "total_chunk_pages": total_chunk_pages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.group_score_chunk_dto import GroupScoreChunkDTO

        d = src_dict.copy()
        group_chunks = []
        _group_chunks = d.pop("group_chunks")
        for group_chunks_item_data in _group_chunks:
            group_chunks_item = GroupScoreChunkDTO.from_dict(group_chunks_item_data)

            group_chunks.append(group_chunks_item)

        total_chunk_pages = d.pop("total_chunk_pages")

        search_over_groups_response_body = cls(
            group_chunks=group_chunks,
            total_chunk_pages=total_chunk_pages,
        )

        search_over_groups_response_body.additional_properties = d
        return search_over_groups_response_body

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
