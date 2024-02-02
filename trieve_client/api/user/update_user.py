from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response_body import ErrorResponseBody
from ...models.slim_user import SlimUser
from ...models.update_user_data import UpdateUserData
from ...types import Response


def _get_kwargs(
    *,
    body: UpdateUserData,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/api/user",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponseBody, SlimUser]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SlimUser.from_dict(response.json())

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
) -> Response[Union[ErrorResponseBody, SlimUser]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateUserData,
) -> Response[Union[ErrorResponseBody, SlimUser]]:
    """update_user

     update_user

    Update a user's information. If the user_id is not provided, the auth'ed user will be updated. If
    the user_id is provided, the auth'ed user must be an admin (1) or owner (2) of the organization.

    Args:
        body (UpdateUserData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, SlimUser]]
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
    client: AuthenticatedClient,
    body: UpdateUserData,
) -> Optional[Union[ErrorResponseBody, SlimUser]]:
    """update_user

     update_user

    Update a user's information. If the user_id is not provided, the auth'ed user will be updated. If
    the user_id is provided, the auth'ed user must be an admin (1) or owner (2) of the organization.

    Args:
        body (UpdateUserData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, SlimUser]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateUserData,
) -> Response[Union[ErrorResponseBody, SlimUser]]:
    """update_user

     update_user

    Update a user's information. If the user_id is not provided, the auth'ed user will be updated. If
    the user_id is provided, the auth'ed user must be an admin (1) or owner (2) of the organization.

    Args:
        body (UpdateUserData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, SlimUser]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UpdateUserData,
) -> Optional[Union[ErrorResponseBody, SlimUser]]:
    """update_user

     update_user

    Update a user's information. If the user_id is not provided, the auth'ed user will be updated. If
    the user_id is provided, the auth'ed user must be an admin (1) or owner (2) of the organization.

    Args:
        body (UpdateUserData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, SlimUser]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
