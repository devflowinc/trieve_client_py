from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_chunk_data import CreateChunkData
from ...models.error_response_body import ErrorResponseBody
from ...models.return_created_chunk import ReturnCreatedChunk
from ...types import Response


def _get_kwargs(
    *,
    body: CreateChunkData,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/chunk",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponseBody, ReturnCreatedChunk]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ReturnCreatedChunk.from_dict(response.json())

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
) -> Response[Union[ErrorResponseBody, ReturnCreatedChunk]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateChunkData,
) -> Response[Union[ErrorResponseBody, ReturnCreatedChunk]]:
    """create_chunk

     create_chunk

    Create a new chunk. If the chunk has the same tracking_id as an existing chunk, the request will
    fail. Once a chunk is created, it can be searched for using the search endpoint.

    Args:
        body (CreateChunkData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, ReturnCreatedChunk]]
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
    body: CreateChunkData,
) -> Optional[Union[ErrorResponseBody, ReturnCreatedChunk]]:
    """create_chunk

     create_chunk

    Create a new chunk. If the chunk has the same tracking_id as an existing chunk, the request will
    fail. Once a chunk is created, it can be searched for using the search endpoint.

    Args:
        body (CreateChunkData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, ReturnCreatedChunk]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateChunkData,
) -> Response[Union[ErrorResponseBody, ReturnCreatedChunk]]:
    """create_chunk

     create_chunk

    Create a new chunk. If the chunk has the same tracking_id as an existing chunk, the request will
    fail. Once a chunk is created, it can be searched for using the search endpoint.

    Args:
        body (CreateChunkData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, ReturnCreatedChunk]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateChunkData,
) -> Optional[Union[ErrorResponseBody, ReturnCreatedChunk]]:
    """create_chunk

     create_chunk

    Create a new chunk. If the chunk has the same tracking_id as an existing chunk, the request will
    fail. Once a chunk is created, it can be searched for using the search endpoint.

    Args:
        body (CreateChunkData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, ReturnCreatedChunk]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
