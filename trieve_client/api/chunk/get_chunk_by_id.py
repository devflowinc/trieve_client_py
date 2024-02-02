from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chunk_metadata import ChunkMetadata
from ...models.error_response_body import ErrorResponseBody
from ...types import Response


def _get_kwargs(
    chunk_id: str,
    *,
    tr_dataset: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["TR-Dataset"] = tr_dataset

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/chunk/{chunk_id}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ChunkMetadata, ErrorResponseBody]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ChunkMetadata.from_dict(response.json())

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
) -> Response[Union[ChunkMetadata, ErrorResponseBody]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chunk_id: str,
    *,
    client: AuthenticatedClient,
    tr_dataset: str,
) -> Response[Union[ChunkMetadata, ErrorResponseBody]]:
    """get_chunk

     get_chunk

    Get a singular chunk by id.

    Args:
        chunk_id (str):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChunkMetadata, ErrorResponseBody]]
    """

    kwargs = _get_kwargs(
        chunk_id=chunk_id,
        tr_dataset=tr_dataset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chunk_id: str,
    *,
    client: AuthenticatedClient,
    tr_dataset: str,
) -> Optional[Union[ChunkMetadata, ErrorResponseBody]]:
    """get_chunk

     get_chunk

    Get a singular chunk by id.

    Args:
        chunk_id (str):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChunkMetadata, ErrorResponseBody]
    """

    return sync_detailed(
        chunk_id=chunk_id,
        client=client,
        tr_dataset=tr_dataset,
    ).parsed


async def asyncio_detailed(
    chunk_id: str,
    *,
    client: AuthenticatedClient,
    tr_dataset: str,
) -> Response[Union[ChunkMetadata, ErrorResponseBody]]:
    """get_chunk

     get_chunk

    Get a singular chunk by id.

    Args:
        chunk_id (str):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChunkMetadata, ErrorResponseBody]]
    """

    kwargs = _get_kwargs(
        chunk_id=chunk_id,
        tr_dataset=tr_dataset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chunk_id: str,
    *,
    client: AuthenticatedClient,
    tr_dataset: str,
) -> Optional[Union[ChunkMetadata, ErrorResponseBody]]:
    """get_chunk

     get_chunk

    Get a singular chunk by id.

    Args:
        chunk_id (str):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChunkMetadata, ErrorResponseBody]
    """

    return (
        await asyncio_detailed(
            chunk_id=chunk_id,
            client=client,
            tr_dataset=tr_dataset,
        )
    ).parsed
