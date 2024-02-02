from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.file import File


T = TypeVar("T", bound="UploadFileResult")


@_attrs_define
class UploadFileResult:
    """
    Attributes:
        file_metadata (File):
    """

    file_metadata: "File"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file_metadata = self.file_metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file_metadata": file_metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file import File

        d = src_dict.copy()
        file_metadata = File.from_dict(d.pop("file_metadata"))

        upload_file_result = cls(
            file_metadata=file_metadata,
        )

        upload_file_result.additional_properties = d
        return upload_file_result

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
