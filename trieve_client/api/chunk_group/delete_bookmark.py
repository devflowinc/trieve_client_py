from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response_body import ErrorResponseBody
from ...types import Response


def _get_kwargs(
    group_id: str,
    bookmark_id: str,
    *,
    tr_dataset: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["TR-Dataset"] = tr_dataset

    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/api/bookmark/{group_id}/{bookmark_id}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponseBody]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResponseBody.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ErrorResponseBody]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: str,
    bookmark_id: str,
    *,
    client: AuthenticatedClient,
    tr_dataset: str,
) -> Response[Union[Any, ErrorResponseBody]]:
    """delete_bookmark

     delete_bookmark

    Route to delete a bookmark. Think of a bookmark as a chunk which is a member of a group.

    Args:
        group_id (str):
        bookmark_id (str):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponseBody]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        bookmark_id=bookmark_id,
        tr_dataset=tr_dataset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: str,
    bookmark_id: str,
    *,
    client: AuthenticatedClient,
    tr_dataset: str,
) -> Optional[Union[Any, ErrorResponseBody]]:
    """delete_bookmark

     delete_bookmark

    Route to delete a bookmark. Think of a bookmark as a chunk which is a member of a group.

    Args:
        group_id (str):
        bookmark_id (str):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponseBody]
    """

    return sync_detailed(
        group_id=group_id,
        bookmark_id=bookmark_id,
        client=client,
        tr_dataset=tr_dataset,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    bookmark_id: str,
    *,
    client: AuthenticatedClient,
    tr_dataset: str,
) -> Response[Union[Any, ErrorResponseBody]]:
    """delete_bookmark

     delete_bookmark

    Route to delete a bookmark. Think of a bookmark as a chunk which is a member of a group.

    Args:
        group_id (str):
        bookmark_id (str):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponseBody]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        bookmark_id=bookmark_id,
        tr_dataset=tr_dataset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    bookmark_id: str,
    *,
    client: AuthenticatedClient,
    tr_dataset: str,
) -> Optional[Union[Any, ErrorResponseBody]]:
    """delete_bookmark

     delete_bookmark

    Route to delete a bookmark. Think of a bookmark as a chunk which is a member of a group.

    Args:
        group_id (str):
        bookmark_id (str):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponseBody]
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            bookmark_id=bookmark_id,
            client=client,
            tr_dataset=tr_dataset,
        )
    ).parsed
