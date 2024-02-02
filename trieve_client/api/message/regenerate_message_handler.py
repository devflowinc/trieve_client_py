from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response_body import ErrorResponseBody
from ...models.regenerate_message_data import RegenerateMessageData
from ...types import Response


def _get_kwargs(
    *,
    body: RegenerateMessageData,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

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
) -> Optional[Union[ErrorResponseBody, str]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = response.text
        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResponseBody.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponseBody, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RegenerateMessageData,
) -> Response[Union[ErrorResponseBody, str]]:
    """regenerate_message

     regenerate_message

    Regenerate the assistant response to the last user message of a topic. This will delete the last
    message and replace it with a new message. The response will include Chunks first on the stream if
    the topic is using RAG. The structure will look like `[chunks]||mesage`. See docs.trieve.ai for more
    information.

    Args:
        body (RegenerateMessageData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, str]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RegenerateMessageData,
) -> Optional[Union[ErrorResponseBody, str]]:
    """regenerate_message

     regenerate_message

    Regenerate the assistant response to the last user message of a topic. This will delete the last
    message and replace it with a new message. The response will include Chunks first on the stream if
    the topic is using RAG. The structure will look like `[chunks]||mesage`. See docs.trieve.ai for more
    information.

    Args:
        body (RegenerateMessageData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, str]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RegenerateMessageData,
) -> Response[Union[ErrorResponseBody, str]]:
    """regenerate_message

     regenerate_message

    Regenerate the assistant response to the last user message of a topic. This will delete the last
    message and replace it with a new message. The response will include Chunks first on the stream if
    the topic is using RAG. The structure will look like `[chunks]||mesage`. See docs.trieve.ai for more
    information.

    Args:
        body (RegenerateMessageData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, str]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RegenerateMessageData,
) -> Optional[Union[ErrorResponseBody, str]]:
    """regenerate_message

     regenerate_message

    Regenerate the assistant response to the last user message of a topic. This will delete the last
    message and replace it with a new message. The response will include Chunks first on the stream if
    the topic is using RAG. The structure will look like `[chunks]||mesage`. See docs.trieve.ai for more
    information.

    Args:
        body (RegenerateMessageData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, str]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
