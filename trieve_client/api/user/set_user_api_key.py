from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response_body import ErrorResponseBody
from ...models.set_user_api_key_request import SetUserApiKeyRequest
from ...models.set_user_api_key_response import SetUserApiKeyResponse
from ...types import Response


def _get_kwargs(
    *,
    body: SetUserApiKeyRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/user/set_api_key",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponseBody, SetUserApiKeyResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SetUserApiKeyResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponseBody, SetUserApiKeyResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SetUserApiKeyRequest,
) -> Response[Union[ErrorResponseBody, SetUserApiKeyResponse]]:
    """set_user_api_key

     set_user_api_key

    Create a new api key for the auth'ed user. Successful response will contain the newly created api
    key. If a write role is assigned the api key will have permission level of the auth'ed user who
    calls this endpoint.

    Args:
        body (SetUserApiKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, SetUserApiKeyResponse]]
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
    body: SetUserApiKeyRequest,
) -> Optional[Union[ErrorResponseBody, SetUserApiKeyResponse]]:
    """set_user_api_key

     set_user_api_key

    Create a new api key for the auth'ed user. Successful response will contain the newly created api
    key. If a write role is assigned the api key will have permission level of the auth'ed user who
    calls this endpoint.

    Args:
        body (SetUserApiKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, SetUserApiKeyResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SetUserApiKeyRequest,
) -> Response[Union[ErrorResponseBody, SetUserApiKeyResponse]]:
    """set_user_api_key

     set_user_api_key

    Create a new api key for the auth'ed user. Successful response will contain the newly created api
    key. If a write role is assigned the api key will have permission level of the auth'ed user who
    calls this endpoint.

    Args:
        body (SetUserApiKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, SetUserApiKeyResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SetUserApiKeyRequest,
) -> Optional[Union[ErrorResponseBody, SetUserApiKeyResponse]]:
    """set_user_api_key

     set_user_api_key

    Create a new api key for the auth'ed user. Successful response will contain the newly created api
    key. If a write role is assigned the api key will have permission level of the auth'ed user who
    calls this endpoint.

    Args:
        body (SetUserApiKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, SetUserApiKeyResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
