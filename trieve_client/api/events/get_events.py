from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response_body import ErrorResponseBody
from ...models.event_return import EventReturn
from ...types import Response


def _get_kwargs(
    page: int,
    *,
    tr_dataset: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["TR-Dataset"] = tr_dataset

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/events/{page}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponseBody, EventReturn]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = EventReturn.from_dict(response.json())

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
) -> Response[Union[ErrorResponseBody, EventReturn]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    page: int,
    *,
    client: AuthenticatedClient,
    tr_dataset: str,
) -> Response[Union[ErrorResponseBody, EventReturn]]:
    """get_events

     get_events

    Get events for the auth'ed user. Currently, this is only for events belonging to the auth'ed user.
    Soon, we plan to associate events to datasets instead of users. Each page contains 10 events.

    Args:
        page (int):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, EventReturn]]
    """

    kwargs = _get_kwargs(
        page=page,
        tr_dataset=tr_dataset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    page: int,
    *,
    client: AuthenticatedClient,
    tr_dataset: str,
) -> Optional[Union[ErrorResponseBody, EventReturn]]:
    """get_events

     get_events

    Get events for the auth'ed user. Currently, this is only for events belonging to the auth'ed user.
    Soon, we plan to associate events to datasets instead of users. Each page contains 10 events.

    Args:
        page (int):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, EventReturn]
    """

    return sync_detailed(
        page=page,
        client=client,
        tr_dataset=tr_dataset,
    ).parsed


async def asyncio_detailed(
    page: int,
    *,
    client: AuthenticatedClient,
    tr_dataset: str,
) -> Response[Union[ErrorResponseBody, EventReturn]]:
    """get_events

     get_events

    Get events for the auth'ed user. Currently, this is only for events belonging to the auth'ed user.
    Soon, we plan to associate events to datasets instead of users. Each page contains 10 events.

    Args:
        page (int):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, EventReturn]]
    """

    kwargs = _get_kwargs(
        page=page,
        tr_dataset=tr_dataset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    page: int,
    *,
    client: AuthenticatedClient,
    tr_dataset: str,
) -> Optional[Union[ErrorResponseBody, EventReturn]]:
    """get_events

     get_events

    Get events for the auth'ed user. Currently, this is only for events belonging to the auth'ed user.
    Soon, we plan to associate events to datasets instead of users. Each page contains 10 events.

    Args:
        page (int):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, EventReturn]
    """

    return (
        await asyncio_detailed(
            page=page,
            client=client,
            tr_dataset=tr_dataset,
        )
    ).parsed
