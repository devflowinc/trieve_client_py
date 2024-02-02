from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.default_error import DefaultError
from ...types import Response


def _get_kwargs(
    subscription_id: str,
    plan_id: str,
    *,
    tr_organization: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["TR-Organization"] = tr_organization

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/api/stripe/subscription_plan/{subscription_id}/{plan_id}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DefaultError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, None)
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
) -> Response[Union[Any, DefaultError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    subscription_id: str,
    plan_id: str,
    *,
    client: AuthenticatedClient,
    tr_organization: str,
) -> Response[Union[Any, DefaultError]]:
    """
    Args:
        subscription_id (str):
        plan_id (str):
        tr_organization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DefaultError]]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        plan_id=plan_id,
        tr_organization=tr_organization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subscription_id: str,
    plan_id: str,
    *,
    client: AuthenticatedClient,
    tr_organization: str,
) -> Optional[Union[Any, DefaultError]]:
    """
    Args:
        subscription_id (str):
        plan_id (str):
        tr_organization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DefaultError]
    """

    return sync_detailed(
        subscription_id=subscription_id,
        plan_id=plan_id,
        client=client,
        tr_organization=tr_organization,
    ).parsed


async def asyncio_detailed(
    subscription_id: str,
    plan_id: str,
    *,
    client: AuthenticatedClient,
    tr_organization: str,
) -> Response[Union[Any, DefaultError]]:
    """
    Args:
        subscription_id (str):
        plan_id (str):
        tr_organization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DefaultError]]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        plan_id=plan_id,
        tr_organization=tr_organization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subscription_id: str,
    plan_id: str,
    *,
    client: AuthenticatedClient,
    tr_organization: str,
) -> Optional[Union[Any, DefaultError]]:
    """
    Args:
        subscription_id (str):
        plan_id (str):
        tr_organization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DefaultError]
    """

    return (
        await asyncio_detailed(
            subscription_id=subscription_id,
            plan_id=plan_id,
            client=client,
            tr_organization=tr_organization,
        )
    ).parsed
