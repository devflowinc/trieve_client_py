from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chunk_metadata_with_file_data import ChunkMetadataWithFileData
from ...models.error_response_body import ErrorResponseBody
from ...models.recommend_chunks_request import RecommendChunksRequest
from ...types import Response


def _get_kwargs(
    *,
    body: RecommendChunksRequest,
    tr_dataset: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["TR-Dataset"] = tr_dataset

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/chunk/recommend",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponseBody, List["ChunkMetadataWithFileData"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ChunkMetadataWithFileData.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[ErrorResponseBody, List["ChunkMetadataWithFileData"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RecommendChunksRequest,
    tr_dataset: str,
) -> Response[Union[ErrorResponseBody, List["ChunkMetadataWithFileData"]]]:
    r"""get_recommended_chunks

     get_recommended_chunks

    Get recommendations of chunks similar to the chunks in the request. Think about this as a feature
    similar to the \"add to playlist\" recommendation feature on Spotify. This request pairs especially
    well with our groups endpoint.

    Args:
        tr_dataset (str):
        body (RecommendChunksRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, List['ChunkMetadataWithFileData']]]
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
    body: RecommendChunksRequest,
    tr_dataset: str,
) -> Optional[Union[ErrorResponseBody, List["ChunkMetadataWithFileData"]]]:
    r"""get_recommended_chunks

     get_recommended_chunks

    Get recommendations of chunks similar to the chunks in the request. Think about this as a feature
    similar to the \"add to playlist\" recommendation feature on Spotify. This request pairs especially
    well with our groups endpoint.

    Args:
        tr_dataset (str):
        body (RecommendChunksRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, List['ChunkMetadataWithFileData']]
    """

    return sync_detailed(
        client=client,
        body=body,
        tr_dataset=tr_dataset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RecommendChunksRequest,
    tr_dataset: str,
) -> Response[Union[ErrorResponseBody, List["ChunkMetadataWithFileData"]]]:
    r"""get_recommended_chunks

     get_recommended_chunks

    Get recommendations of chunks similar to the chunks in the request. Think about this as a feature
    similar to the \"add to playlist\" recommendation feature on Spotify. This request pairs especially
    well with our groups endpoint.

    Args:
        tr_dataset (str):
        body (RecommendChunksRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, List['ChunkMetadataWithFileData']]]
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
    body: RecommendChunksRequest,
    tr_dataset: str,
) -> Optional[Union[ErrorResponseBody, List["ChunkMetadataWithFileData"]]]:
    r"""get_recommended_chunks

     get_recommended_chunks

    Get recommendations of chunks similar to the chunks in the request. Think about this as a feature
    similar to the \"add to playlist\" recommendation feature on Spotify. This request pairs especially
    well with our groups endpoint.

    Args:
        tr_dataset (str):
        body (RecommendChunksRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, List['ChunkMetadataWithFileData']]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            tr_dataset=tr_dataset,
        )
    ).parsed
