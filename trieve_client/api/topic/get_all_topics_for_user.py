from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response_body import ErrorResponseBody
from ...models.topic import Topic
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    tr_dataset: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["TR-Dataset"] = tr_dataset

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/topic/user/{user_id}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponseBody, List["Topic"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Topic.from_dict(response_200_item_data)

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
) -> Response[Union[ErrorResponseBody, List["Topic"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    tr_dataset: str,
) -> Response[Union[ErrorResponseBody, List["Topic"]]]:
    """get_all_topics_for_user

     get_all_topics_for_user

    Get all topics belonging to a the auth'ed user. Soon, we plan to allow specification of the user for
    this route and include pagination.

    Args:
        user_id (str):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, List['Topic']]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        tr_dataset=tr_dataset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient,
    tr_dataset: str,
) -> Optional[Union[ErrorResponseBody, List["Topic"]]]:
    """get_all_topics_for_user

     get_all_topics_for_user

    Get all topics belonging to a the auth'ed user. Soon, we plan to allow specification of the user for
    this route and include pagination.

    Args:
        user_id (str):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, List['Topic']]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        tr_dataset=tr_dataset,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    tr_dataset: str,
) -> Response[Union[ErrorResponseBody, List["Topic"]]]:
    """get_all_topics_for_user

     get_all_topics_for_user

    Get all topics belonging to a the auth'ed user. Soon, we plan to allow specification of the user for
    this route and include pagination.

    Args:
        user_id (str):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, List['Topic']]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        tr_dataset=tr_dataset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
    tr_dataset: str,
) -> Optional[Union[ErrorResponseBody, List["Topic"]]]:
    """get_all_topics_for_user

     get_all_topics_for_user

    Get all topics belonging to a the auth'ed user. Soon, we plan to allow specification of the user for
    this route and include pagination.

    Args:
        user_id (str):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, List['Topic']]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            tr_dataset=tr_dataset,
        )
    ).parsed
