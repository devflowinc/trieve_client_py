from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bookmark_data import BookmarkData
from ...models.error_response_body import ErrorResponseBody
from ...types import Response


def _get_kwargs(
    group_id: str,
    page: int,
    *,
    tr_dataset: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["TR-Dataset"] = tr_dataset

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/chunk_group/{group_id}/{page}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BookmarkData, ErrorResponseBody]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = BookmarkData.from_dict(response.json())

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
) -> Response[Union[BookmarkData, ErrorResponseBody]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: str,
    page: int,
    *,
    client: AuthenticatedClient,
    tr_dataset: str,
) -> Response[Union[BookmarkData, ErrorResponseBody]]:
    """get_all_bookmarks

     get_all_bookmarks

    Route to get all bookmarks for a group. Think of a bookmark as a chunk which is a member of a group.
    The response is paginated, with each page containing 10 chunks (bookmarks). Support for custom page
    size is coming soon.

    Args:
        group_id (str):
        page (int):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BookmarkData, ErrorResponseBody]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        page=page,
        tr_dataset=tr_dataset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: str,
    page: int,
    *,
    client: AuthenticatedClient,
    tr_dataset: str,
) -> Optional[Union[BookmarkData, ErrorResponseBody]]:
    """get_all_bookmarks

     get_all_bookmarks

    Route to get all bookmarks for a group. Think of a bookmark as a chunk which is a member of a group.
    The response is paginated, with each page containing 10 chunks (bookmarks). Support for custom page
    size is coming soon.

    Args:
        group_id (str):
        page (int):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BookmarkData, ErrorResponseBody]
    """

    return sync_detailed(
        group_id=group_id,
        page=page,
        client=client,
        tr_dataset=tr_dataset,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    page: int,
    *,
    client: AuthenticatedClient,
    tr_dataset: str,
) -> Response[Union[BookmarkData, ErrorResponseBody]]:
    """get_all_bookmarks

     get_all_bookmarks

    Route to get all bookmarks for a group. Think of a bookmark as a chunk which is a member of a group.
    The response is paginated, with each page containing 10 chunks (bookmarks). Support for custom page
    size is coming soon.

    Args:
        group_id (str):
        page (int):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BookmarkData, ErrorResponseBody]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        page=page,
        tr_dataset=tr_dataset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    page: int,
    *,
    client: AuthenticatedClient,
    tr_dataset: str,
) -> Optional[Union[BookmarkData, ErrorResponseBody]]:
    """get_all_bookmarks

     get_all_bookmarks

    Route to get all bookmarks for a group. Think of a bookmark as a chunk which is a member of a group.
    The response is paginated, with each page containing 10 chunks (bookmarks). Support for custom page
    size is coming soon.

    Args:
        group_id (str):
        page (int):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BookmarkData, ErrorResponseBody]
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            page=page,
            client=client,
            tr_dataset=tr_dataset,
        )
    ).parsed
