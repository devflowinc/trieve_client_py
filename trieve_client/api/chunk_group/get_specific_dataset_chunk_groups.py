from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response_body import ErrorResponseBody
from ...models.group_data import GroupData
from ...types import Response


def _get_kwargs(
    dataset_id: str,
    page: int,
    *,
    tr_dataset: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["TR-Dataset"] = tr_dataset

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/dataset/groups/{dataset_id}/{page}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponseBody, GroupData]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GroupData.from_dict(response.json())

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
) -> Response[Union[ErrorResponseBody, GroupData]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataset_id: str,
    page: int,
    *,
    client: AuthenticatedClient,
    tr_dataset: str,
) -> Response[Union[ErrorResponseBody, GroupData]]:
    """get_dataset_groups

     get_dataset_groups

    Fetch the groups which belong to a dataset specified by its id.

    Args:
        dataset_id (str):
        page (int):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, GroupData]]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        page=page,
        tr_dataset=tr_dataset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataset_id: str,
    page: int,
    *,
    client: AuthenticatedClient,
    tr_dataset: str,
) -> Optional[Union[ErrorResponseBody, GroupData]]:
    """get_dataset_groups

     get_dataset_groups

    Fetch the groups which belong to a dataset specified by its id.

    Args:
        dataset_id (str):
        page (int):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, GroupData]
    """

    return sync_detailed(
        dataset_id=dataset_id,
        page=page,
        client=client,
        tr_dataset=tr_dataset,
    ).parsed


async def asyncio_detailed(
    dataset_id: str,
    page: int,
    *,
    client: AuthenticatedClient,
    tr_dataset: str,
) -> Response[Union[ErrorResponseBody, GroupData]]:
    """get_dataset_groups

     get_dataset_groups

    Fetch the groups which belong to a dataset specified by its id.

    Args:
        dataset_id (str):
        page (int):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, GroupData]]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        page=page,
        tr_dataset=tr_dataset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataset_id: str,
    page: int,
    *,
    client: AuthenticatedClient,
    tr_dataset: str,
) -> Optional[Union[ErrorResponseBody, GroupData]]:
    """get_dataset_groups

     get_dataset_groups

    Fetch the groups which belong to a dataset specified by its id.

    Args:
        dataset_id (str):
        page (int):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, GroupData]
    """

    return (
        await asyncio_detailed(
            dataset_id=dataset_id,
            page=page,
            client=client,
            tr_dataset=tr_dataset,
        )
    ).parsed
