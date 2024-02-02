from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response_body import ErrorResponseBody
from ...models.organization import Organization
from ...types import Response


def _get_kwargs(
    organization_id: str,
    *,
    tr_organization: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["TR-Organization"] = tr_organization

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/organization/{organization_id}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponseBody, Organization]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Organization.from_dict(response.json())

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
) -> Response[Union[ErrorResponseBody, Organization]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    tr_organization: str,
) -> Response[Union[ErrorResponseBody, Organization]]:
    """get_organization

     get_organization

    Fetch the details of an organization by its id. The auth'ed user must be an admin or owner of the
    organization to fetch it.

    Args:
        organization_id (str):
        tr_organization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, Organization]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        tr_organization=tr_organization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    tr_organization: str,
) -> Optional[Union[ErrorResponseBody, Organization]]:
    """get_organization

     get_organization

    Fetch the details of an organization by its id. The auth'ed user must be an admin or owner of the
    organization to fetch it.

    Args:
        organization_id (str):
        tr_organization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, Organization]
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        tr_organization=tr_organization,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    tr_organization: str,
) -> Response[Union[ErrorResponseBody, Organization]]:
    """get_organization

     get_organization

    Fetch the details of an organization by its id. The auth'ed user must be an admin or owner of the
    organization to fetch it.

    Args:
        organization_id (str):
        tr_organization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, Organization]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        tr_organization=tr_organization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    tr_organization: str,
) -> Optional[Union[ErrorResponseBody, Organization]]:
    """get_organization

     get_organization

    Fetch the details of an organization by its id. The auth'ed user must be an admin or owner of the
    organization to fetch it.

    Args:
        organization_id (str):
        tr_organization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, Organization]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            tr_organization=tr_organization,
        )
    ).parsed
