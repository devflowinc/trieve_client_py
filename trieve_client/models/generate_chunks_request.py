from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_message_proxy import ChatMessageProxy


T = TypeVar("T", bound="GenerateChunksRequest")


@_attrs_define
class GenerateChunksRequest:
    """
    Attributes:
        chunk_ids (List[str]): The ids of the chunks to be retrieved and injected into the context window for RAG.
        prev_messages (List['ChatMessageProxy']): The previous messages to be placed into the chat history. The last
            message in this array will be the prompt for the model to inference on. The length of this array must be at
            least 1.
        model (Union[None, Unset, str]): The model to use for the chat. This can be any model from the openrouter model
            list. If no model is provided, gryphe/mythomax-l2-13b will be used.
        prompt (Union[None, Unset, str]): Prompt for the last message in the prev_messages array. This will be used to
            generate the next message in the chat. The default is 'Respond to the instruction and include the doc numbers
            that you used in square brackets at the end of the sentences that you used the docs for:'. You can also specify
            an empty string to leave the final message alone such that your user's final message can be used as the prompt.
            See docs.trieve.ai or contact us for more information.
        stream_response (Union[None, Unset, bool]): Whether or not to stream the response. If this is set to true or not
            included, the response will be a stream. If this is set to false, the response will be a normal JSON response.
            Default is true.
    """

    chunk_ids: List[str]
    prev_messages: List["ChatMessageProxy"]
    model: Union[None, Unset, str] = UNSET
    prompt: Union[None, Unset, str] = UNSET
    stream_response: Union[None, Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        chunk_ids = self.chunk_ids

        prev_messages = []
        for prev_messages_item_data in self.prev_messages:
            prev_messages_item = prev_messages_item_data.to_dict()
            prev_messages.append(prev_messages_item)

        model: Union[None, Unset, str]
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        prompt: Union[None, Unset, str]
        if isinstance(self.prompt, Unset):
            prompt = UNSET
        else:
            prompt = self.prompt

        stream_response: Union[None, Unset, bool]
        if isinstance(self.stream_response, Unset):
            stream_response = UNSET
        else:
            stream_response = self.stream_response

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chunk_ids": chunk_ids,
                "prev_messages": prev_messages,
            }
        )
        if model is not UNSET:
            field_dict["model"] = model
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if stream_response is not UNSET:
            field_dict["stream_response"] = stream_response

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.chat_message_proxy import ChatMessageProxy

        d = src_dict.copy()
        chunk_ids = cast(List[str], d.pop("chunk_ids"))

        prev_messages = []
        _prev_messages = d.pop("prev_messages")
        for prev_messages_item_data in _prev_messages:
            prev_messages_item = ChatMessageProxy.from_dict(prev_messages_item_data)

            prev_messages.append(prev_messages_item)

        def _parse_model(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        model = _parse_model(d.pop("model", UNSET))

        def _parse_prompt(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        prompt = _parse_prompt(d.pop("prompt", UNSET))

        def _parse_stream_response(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        stream_response = _parse_stream_response(d.pop("stream_response", UNSET))

        generate_chunks_request = cls(
            chunk_ids=chunk_ids,
            prev_messages=prev_messages,
            model=model,
            prompt=prompt,
            stream_response=stream_response,
        )

        generate_chunks_request.additional_properties = d
        return generate_chunks_request

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
