from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response_body import ErrorResponseBody
from ...models.search_chunk_data import SearchChunkData
from ...models.search_over_groups_response_body import SearchOverGroupsResponseBody
from ...types import Response


def _get_kwargs(
    *,
    body: SearchChunkData,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/chunk_group/search_over_groups",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponseBody, SearchOverGroupsResponseBody]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SearchOverGroupsResponseBody.from_dict(response.json())

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
) -> Response[Union[ErrorResponseBody, SearchOverGroupsResponseBody]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SearchChunkData,
) -> Response[Union[ErrorResponseBody, SearchOverGroupsResponseBody]]:
    """group_oriented_search

     group_oriented_search

    This route allows you to get groups as results instead of chunks. Each group returned will have the
    matching chunks sorted by similarity within the group. This is useful for when you want to get
    groups of chunks which are similar to the search query. If choosing hybrid search, the results will
    be re-ranked using BAAI/bge-reranker-large. Compatible with semantic, fulltext, or hybrid search
    modes.

    Args:
        body (SearchChunkData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, SearchOverGroupsResponseBody]]
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
    body: SearchChunkData,
) -> Optional[Union[ErrorResponseBody, SearchOverGroupsResponseBody]]:
    """group_oriented_search

     group_oriented_search

    This route allows you to get groups as results instead of chunks. Each group returned will have the
    matching chunks sorted by similarity within the group. This is useful for when you want to get
    groups of chunks which are similar to the search query. If choosing hybrid search, the results will
    be re-ranked using BAAI/bge-reranker-large. Compatible with semantic, fulltext, or hybrid search
    modes.

    Args:
        body (SearchChunkData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, SearchOverGroupsResponseBody]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SearchChunkData,
) -> Response[Union[ErrorResponseBody, SearchOverGroupsResponseBody]]:
    """group_oriented_search

     group_oriented_search

    This route allows you to get groups as results instead of chunks. Each group returned will have the
    matching chunks sorted by similarity within the group. This is useful for when you want to get
    groups of chunks which are similar to the search query. If choosing hybrid search, the results will
    be re-ranked using BAAI/bge-reranker-large. Compatible with semantic, fulltext, or hybrid search
    modes.

    Args:
        body (SearchChunkData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, SearchOverGroupsResponseBody]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SearchChunkData,
) -> Optional[Union[ErrorResponseBody, SearchOverGroupsResponseBody]]:
    """group_oriented_search

     group_oriented_search

    This route allows you to get groups as results instead of chunks. Each group returned will have the
    matching chunks sorted by similarity within the group. This is useful for when you want to get
    groups of chunks which are similar to the search query. If choosing hybrid search, the results will
    be re-ranked using BAAI/bge-reranker-large. Compatible with semantic, fulltext, or hybrid search
    modes.

    Args:
        body (SearchChunkData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, SearchOverGroupsResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
