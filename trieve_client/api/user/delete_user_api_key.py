from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_key_dto import ApiKeyDTO
from ...models.default_error import DefaultError
from ...models.delete_user_api_key_request import DeleteUserApiKeyRequest
from ...types import Response


def _get_kwargs(
    *,
    body: DeleteUserApiKeyRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": "/api/user/delete_api_key",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DefaultError, List["ApiKeyDTO"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ApiKeyDTO.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = DefaultError.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[DefaultError, List["ApiKeyDTO"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: DeleteUserApiKeyRequest,
) -> Response[Union[DefaultError, List["ApiKeyDTO"]]]:
    """delete_user_api_key

     delete_user_api_key

    Delete an api key for the auth'ed user.

    Args:
        body (DeleteUserApiKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DefaultError, List['ApiKeyDTO']]]
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
    body: DeleteUserApiKeyRequest,
) -> Optional[Union[DefaultError, List["ApiKeyDTO"]]]:
    """delete_user_api_key

     delete_user_api_key

    Delete an api key for the auth'ed user.

    Args:
        body (DeleteUserApiKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DefaultError, List['ApiKeyDTO']]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: DeleteUserApiKeyRequest,
) -> Response[Union[DefaultError, List["ApiKeyDTO"]]]:
    """delete_user_api_key

     delete_user_api_key

    Delete an api key for the auth'ed user.

    Args:
        body (DeleteUserApiKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DefaultError, List['ApiKeyDTO']]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: DeleteUserApiKeyRequest,
) -> Optional[Union[DefaultError, List["ApiKeyDTO"]]]:
    """delete_user_api_key

     delete_user_api_key

    Delete an api key for the auth'ed user.

    Args:
        body (DeleteUserApiKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DefaultError, List['ApiKeyDTO']]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
