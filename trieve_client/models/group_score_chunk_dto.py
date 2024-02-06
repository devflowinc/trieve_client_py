from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.score_chunk_dto import ScoreChunkDTO


T = TypeVar("T", bound="GroupScoreChunkDTO")


@_attrs_define
class GroupScoreChunkDTO:
    """
    Attributes:
        group_id (str):
        metadata (List['ScoreChunkDTO']):
    """

    group_id: str
    metadata: List["ScoreChunkDTO"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group_id = self.group_id

        metadata = []
        for metadata_item_data in self.metadata:
            metadata_item = metadata_item_data.to_dict()
            metadata.append(metadata_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "group_id": group_id,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.score_chunk_dto import ScoreChunkDTO

        d = src_dict.copy()
        group_id = d.pop("group_id")

        metadata = []
        _metadata = d.pop("metadata")
        for metadata_item_data in _metadata:
            metadata_item = ScoreChunkDTO.from_dict(metadata_item_data)

            metadata.append(metadata_item)

        group_score_chunk_dto = cls(
            group_id=group_id,
            metadata=metadata,
        )

        group_score_chunk_dto.additional_properties = d
        return group_score_chunk_dto

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
