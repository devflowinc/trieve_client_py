from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataset import Dataset
from ...models.error_response_body import ErrorResponseBody
from ...models.update_dataset_request import UpdateDatasetRequest
from ...types import Response


def _get_kwargs(
    *,
    body: UpdateDatasetRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/api/dataset",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Dataset, ErrorResponseBody]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Dataset.from_dict(response.json())

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
) -> Response[Union[Dataset, ErrorResponseBody]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateDatasetRequest,
) -> Response[Union[Dataset, ErrorResponseBody]]:
    """update_dataset

     update_dataset

    Update a dataset. The auth'ed user must be an owner of the organization to update a dataset.

    Args:
        body (UpdateDatasetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Dataset, ErrorResponseBody]]
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
    client: Union[AuthenticatedClient, Client],
    body: UpdateDatasetRequest,
) -> Optional[Union[Dataset, ErrorResponseBody]]:
    """update_dataset

     update_dataset

    Update a dataset. The auth'ed user must be an owner of the organization to update a dataset.

    Args:
        body (UpdateDatasetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Dataset, ErrorResponseBody]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateDatasetRequest,
) -> Response[Union[Dataset, ErrorResponseBody]]:
    """update_dataset

     update_dataset

    Update a dataset. The auth'ed user must be an owner of the organization to update a dataset.

    Args:
        body (UpdateDatasetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Dataset, ErrorResponseBody]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateDatasetRequest,
) -> Optional[Union[Dataset, ErrorResponseBody]]:
    """update_dataset

     update_dataset

    Update a dataset. The auth'ed user must be an owner of the organization to update a dataset.

    Args:
        body (UpdateDatasetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Dataset, ErrorResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
