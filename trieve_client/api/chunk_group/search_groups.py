from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response_body import ErrorResponseBody
from ...models.search_groups_data import SearchGroupsData
from ...models.search_groups_result import SearchGroupsResult
from ...types import Response


def _get_kwargs(
    *,
    body: SearchGroupsData,
    tr_dataset: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["TR-Dataset"] = tr_dataset

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/chunk_group/search",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponseBody, SearchGroupsResult]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SearchGroupsResult.from_dict(response.json())

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
) -> Response[Union[ErrorResponseBody, SearchGroupsResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SearchGroupsData,
    tr_dataset: str,
) -> Response[Union[ErrorResponseBody, SearchGroupsResult]]:
    """group_search

     group_search

    This route allows you to search only within a group. This is useful for when you only want search
    results to contain chunks which are members of a specific group. Think about this like searching
    within a playlist or bookmark folder.

    Args:
        tr_dataset (str):
        body (SearchGroupsData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, SearchGroupsResult]]
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
    body: SearchGroupsData,
    tr_dataset: str,
) -> Optional[Union[ErrorResponseBody, SearchGroupsResult]]:
    """group_search

     group_search

    This route allows you to search only within a group. This is useful for when you only want search
    results to contain chunks which are members of a specific group. Think about this like searching
    within a playlist or bookmark folder.

    Args:
        tr_dataset (str):
        body (SearchGroupsData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, SearchGroupsResult]
    """

    return sync_detailed(
        client=client,
        body=body,
        tr_dataset=tr_dataset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SearchGroupsData,
    tr_dataset: str,
) -> Response[Union[ErrorResponseBody, SearchGroupsResult]]:
    """group_search

     group_search

    This route allows you to search only within a group. This is useful for when you only want search
    results to contain chunks which are members of a specific group. Think about this like searching
    within a playlist or bookmark folder.

    Args:
        tr_dataset (str):
        body (SearchGroupsData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, SearchGroupsResult]]
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
    body: SearchGroupsData,
    tr_dataset: str,
) -> Optional[Union[ErrorResponseBody, SearchGroupsResult]]:
    """group_search

     group_search

    This route allows you to search only within a group. This is useful for when you only want search
    results to contain chunks which are members of a specific group. Think about this like searching
    within a playlist or bookmark folder.

    Args:
        tr_dataset (str):
        body (SearchGroupsData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, SearchGroupsResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            tr_dataset=tr_dataset,
        )
    ).parsed
