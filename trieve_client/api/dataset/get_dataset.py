from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataset import Dataset
from ...models.error_response_body import ErrorResponseBody
from ...types import Response


def _get_kwargs(
    dataset_id: str,
    *,
    tr_organization: str,
    tr_dataset: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["TR-Organization"] = tr_organization

    headers["TR-Dataset"] = tr_dataset

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/dataset/{dataset_id}",
    }

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
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    tr_organization: str,
    tr_dataset: str,
) -> Response[Union[Dataset, ErrorResponseBody]]:
    """get_dataset

     get_dataset

    Get a dataset by id. The auth'ed user must be an admin or owner of the organization to get a
    dataset.

    Args:
        dataset_id (str):
        tr_organization (str):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Dataset, ErrorResponseBody]]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        tr_organization=tr_organization,
        tr_dataset=tr_dataset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    tr_organization: str,
    tr_dataset: str,
) -> Optional[Union[Dataset, ErrorResponseBody]]:
    """get_dataset

     get_dataset

    Get a dataset by id. The auth'ed user must be an admin or owner of the organization to get a
    dataset.

    Args:
        dataset_id (str):
        tr_organization (str):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Dataset, ErrorResponseBody]
    """

    return sync_detailed(
        dataset_id=dataset_id,
        client=client,
        tr_organization=tr_organization,
        tr_dataset=tr_dataset,
    ).parsed


async def asyncio_detailed(
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    tr_organization: str,
    tr_dataset: str,
) -> Response[Union[Dataset, ErrorResponseBody]]:
    """get_dataset

     get_dataset

    Get a dataset by id. The auth'ed user must be an admin or owner of the organization to get a
    dataset.

    Args:
        dataset_id (str):
        tr_organization (str):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Dataset, ErrorResponseBody]]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        tr_organization=tr_organization,
        tr_dataset=tr_dataset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    tr_organization: str,
    tr_dataset: str,
) -> Optional[Union[Dataset, ErrorResponseBody]]:
    """get_dataset

     get_dataset

    Get a dataset by id. The auth'ed user must be an admin or owner of the organization to get a
    dataset.

    Args:
        dataset_id (str):
        tr_organization (str):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Dataset, ErrorResponseBody]
    """

    return (
        await asyncio_detailed(
            dataset_id=dataset_id,
            client=client,
            tr_organization=tr_organization,
            tr_dataset=tr_dataset,
        )
    ).parsed
