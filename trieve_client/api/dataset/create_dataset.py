from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_dataset_request import CreateDatasetRequest
from ...models.dataset import Dataset
from ...models.default_error import DefaultError
from ...types import Response


def _get_kwargs(
    *,
    body: CreateDatasetRequest,
    tr_organization: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["TR-Organization"] = tr_organization

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/dataset",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Dataset, DefaultError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Dataset.from_dict(response.json())

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
) -> Response[Union[Dataset, DefaultError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateDatasetRequest,
    tr_organization: str,
) -> Response[Union[Dataset, DefaultError]]:
    """create_dataset

     create_dataset

    Create a new dataset. The auth'ed user must be an owner of the organization to create a dataset.

    Args:
        tr_organization (str):
        body (CreateDatasetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Dataset, DefaultError]]
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
    body: CreateDatasetRequest,
    tr_organization: str,
) -> Optional[Union[Dataset, DefaultError]]:
    """create_dataset

     create_dataset

    Create a new dataset. The auth'ed user must be an owner of the organization to create a dataset.

    Args:
        tr_organization (str):
        body (CreateDatasetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Dataset, DefaultError]
    """

    return sync_detailed(
        client=client,
        body=body,
        tr_organization=tr_organization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateDatasetRequest,
    tr_organization: str,
) -> Response[Union[Dataset, DefaultError]]:
    """create_dataset

     create_dataset

    Create a new dataset. The auth'ed user must be an owner of the organization to create a dataset.

    Args:
        tr_organization (str):
        body (CreateDatasetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Dataset, DefaultError]]
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
    body: CreateDatasetRequest,
    tr_organization: str,
) -> Optional[Union[Dataset, DefaultError]]:
    """create_dataset

     create_dataset

    Create a new dataset. The auth'ed user must be an owner of the organization to create a dataset.

    Args:
        tr_organization (str):
        body (CreateDatasetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Dataset, DefaultError]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            tr_organization=tr_organization,
        )
    ).parsed
