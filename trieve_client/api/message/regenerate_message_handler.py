from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.default_error import DefaultError
from ...models.regenerate_message_data import RegenerateMessageData
from ...types import Response


def _get_kwargs(
    *,
    body: RegenerateMessageData,
    tr_dataset: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["TR-Dataset"] = tr_dataset

    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": "/api/message",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DefaultError, str]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = response.text
        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = DefaultError.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[DefaultError, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RegenerateMessageData,
    tr_dataset: str,
) -> Response[Union[DefaultError, str]]:
    """regenerate_message

     regenerate_message

    Regenerate the assistant response to the last user message of a topic. This will delete the last
    message and replace it with a new message. The response will include Chunks first on the stream if
    the topic is using RAG. The structure will look like `[chunks]||mesage`. See docs.trieve.ai for more
    information.

    Args:
        tr_dataset (str):
        body (RegenerateMessageData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DefaultError, str]]
    """

    kwargs = _get_kwargs(
        body=body,
        tr_dataset=tr_dataset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: RegenerateMessageData,
    tr_dataset: str,
) -> Optional[Union[DefaultError, str]]:
    """regenerate_message

     regenerate_message

    Regenerate the assistant response to the last user message of a topic. This will delete the last
    message and replace it with a new message. The response will include Chunks first on the stream if
    the topic is using RAG. The structure will look like `[chunks]||mesage`. See docs.trieve.ai for more
    information.

    Args:
        tr_dataset (str):
        body (RegenerateMessageData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DefaultError, str]
    """

    return sync_detailed(
        client=client,
        body=body,
        tr_dataset=tr_dataset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RegenerateMessageData,
    tr_dataset: str,
) -> Response[Union[DefaultError, str]]:
    """regenerate_message

     regenerate_message

    Regenerate the assistant response to the last user message of a topic. This will delete the last
    message and replace it with a new message. The response will include Chunks first on the stream if
    the topic is using RAG. The structure will look like `[chunks]||mesage`. See docs.trieve.ai for more
    information.

    Args:
        tr_dataset (str):
        body (RegenerateMessageData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DefaultError, str]]
    """

    kwargs = _get_kwargs(
        body=body,
        tr_dataset=tr_dataset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RegenerateMessageData,
    tr_dataset: str,
) -> Optional[Union[DefaultError, str]]:
    """regenerate_message

     regenerate_message

    Regenerate the assistant response to the last user message of a topic. This will delete the last
    message and replace it with a new message. The response will include Chunks first on the stream if
    the topic is using RAG. The structure will look like `[chunks]||mesage`. See docs.trieve.ai for more
    information.

    Args:
        tr_dataset (str):
        body (RegenerateMessageData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DefaultError, str]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            tr_dataset=tr_dataset,
        )
    ).parsed
