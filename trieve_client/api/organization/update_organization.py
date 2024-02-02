from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.default_error import DefaultError
from ...models.organization import Organization
from ...models.update_organization_data import UpdateOrganizationData
from ...types import Response


def _get_kwargs(
    *,
    body: UpdateOrganizationData,
    tr_organization: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["TR-Organization"] = tr_organization

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/api/organization",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DefaultError, Organization]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Organization.from_dict(response.json())

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
) -> Response[Union[DefaultError, Organization]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateOrganizationData,
    tr_organization: str,
) -> Response[Union[DefaultError, Organization]]:
    """update_organization

     update_organization

    Update an organization. Only the owner of the organization can update it.

    Args:
        tr_organization (str):
        body (UpdateOrganizationData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DefaultError, Organization]]
    """

    kwargs = _get_kwargs(
        body=body,
        tr_organization=tr_organization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: UpdateOrganizationData,
    tr_organization: str,
) -> Optional[Union[DefaultError, Organization]]:
    """update_organization

     update_organization

    Update an organization. Only the owner of the organization can update it.

    Args:
        tr_organization (str):
        body (UpdateOrganizationData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DefaultError, Organization]
    """

    return sync_detailed(
        client=client,
        body=body,
        tr_organization=tr_organization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateOrganizationData,
    tr_organization: str,
) -> Response[Union[DefaultError, Organization]]:
    """update_organization

     update_organization

    Update an organization. Only the owner of the organization can update it.

    Args:
        tr_organization (str):
        body (UpdateOrganizationData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DefaultError, Organization]]
    """

    kwargs = _get_kwargs(
        body=body,
        tr_organization=tr_organization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UpdateOrganizationData,
    tr_organization: str,
) -> Optional[Union[DefaultError, Organization]]:
    """update_organization

     update_organization

    Update an organization. Only the owner of the organization can update it.

    Args:
        tr_organization (str):
        body (UpdateOrganizationData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DefaultError, Organization]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            tr_organization=tr_organization,
        )
    ).parsed
