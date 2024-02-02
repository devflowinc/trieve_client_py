from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bookmark_chunks import BookmarkChunks
    from ..models.chunk_group import ChunkGroup


T = TypeVar("T", bound="BookmarkData")


@_attrs_define
class BookmarkData:
    """
    Attributes:
        bookmarks (List['BookmarkChunks']):
        group (ChunkGroup):
        total_pages (int):
    """

    bookmarks: List["BookmarkChunks"]
    group: "ChunkGroup"
    total_pages: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bookmarks = []
        for bookmarks_item_data in self.bookmarks:
            bookmarks_item = bookmarks_item_data.to_dict()
            bookmarks.append(bookmarks_item)

        group = self.group.to_dict()

        total_pages = self.total_pages

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bookmarks": bookmarks,
                "group": group,
                "total_pages": total_pages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bookmark_chunks import BookmarkChunks
        from ..models.chunk_group import ChunkGroup

        d = src_dict.copy()
        bookmarks = []
        _bookmarks = d.pop("bookmarks")
        for bookmarks_item_data in _bookmarks:
            bookmarks_item = BookmarkChunks.from_dict(bookmarks_item_data)

            bookmarks.append(bookmarks_item)

        group = ChunkGroup.from_dict(d.pop("group"))

        total_pages = d.pop("total_pages")

        bookmark_data = cls(
            bookmarks=bookmarks,
            group=group,
            total_pages=total_pages,
        )

        bookmark_data.additional_properties = d
        return bookmark_data

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
