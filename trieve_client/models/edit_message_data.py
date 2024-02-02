from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditMessageData")


@_attrs_define
class EditMessageData:
    r"""
    Attributes:
        message_sort_order (int): The sort order of the message to edit.
        new_message_content (str): The new content of the message to replace the old content with.
        topic_id (str): The id of the topic to edit the message at the given sort order for.
        highlight_citations (Union[None, Unset, bool]): Whether or not to highlight the citations in the response. If
            this is set to true or not included, the citations will be highlighted. If this is set to false, the citations
            will not be highlighted. Default is true.
        highlight_delimiters (Union[List[str], None, Unset]): The delimiters to use for highlighting the citations. If
            this is not included, the default delimiters will be used. Default is `[".", "!", "?", "\n", "\t", ","]`.
        model (Union[None, Unset, str]): The model to use for the assistant generative inferences. This can be any model
            from the openrouter model list. If no model is provided, the gryphe/mythomax-l2-13b will be used.~
        stream_response (Union[None, Unset, bool]): Whether or not to stream the response. If this is set to true or not
            included, the response will be a stream. If this is set to false, the response will be a normal JSON response.
            Default is true.
    """

    message_sort_order: int
    new_message_content: str
    topic_id: str
    highlight_citations: Union[None, Unset, bool] = UNSET
    highlight_delimiters: Union[List[str], None, Unset] = UNSET
    model: Union[None, Unset, str] = UNSET
    stream_response: Union[None, Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message_sort_order = self.message_sort_order

        new_message_content = self.new_message_content

        topic_id = self.topic_id

        highlight_citations: Union[None, Unset, bool]
        if isinstance(self.highlight_citations, Unset):
            highlight_citations = UNSET
        else:
            highlight_citations = self.highlight_citations

        highlight_delimiters: Union[List[str], None, Unset]
        if isinstance(self.highlight_delimiters, Unset):
            highlight_delimiters = UNSET
        elif isinstance(self.highlight_delimiters, list):
            highlight_delimiters = self.highlight_delimiters

        else:
            highlight_delimiters = self.highlight_delimiters

        model: Union[None, Unset, str]
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        stream_response: Union[None, Unset, bool]
        if isinstance(self.stream_response, Unset):
            stream_response = UNSET
        else:
            stream_response = self.stream_response

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message_sort_order": message_sort_order,
                "new_message_content": new_message_content,
                "topic_id": topic_id,
            }
        )
        if highlight_citations is not UNSET:
            field_dict["highlight_citations"] = highlight_citations
        if highlight_delimiters is not UNSET:
            field_dict["highlight_delimiters"] = highlight_delimiters
        if model is not UNSET:
            field_dict["model"] = model
        if stream_response is not UNSET:
            field_dict["stream_response"] = stream_response

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message_sort_order = d.pop("message_sort_order")

        new_message_content = d.pop("new_message_content")

        topic_id = d.pop("topic_id")

        def _parse_highlight_citations(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        highlight_citations = _parse_highlight_citations(d.pop("highlight_citations", UNSET))

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

        def _parse_model(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        model = _parse_model(d.pop("model", UNSET))

        def _parse_stream_response(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        stream_response = _parse_stream_response(d.pop("stream_response", UNSET))

        edit_message_data = cls(
            message_sort_order=message_sort_order,
            new_message_content=new_message_content,
            topic_id=topic_id,
            highlight_citations=highlight_citations,
            highlight_delimiters=highlight_delimiters,
            model=model,
            stream_response=stream_response,
        )

        edit_message_data.additional_properties = d
        return edit_message_data

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
