from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response_body import ErrorResponseBody
from ...models.file_dto import FileDTO
from ...types import Response


def _get_kwargs(
    file_id: str,
    *,
    tr_dataset: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["TR-Dataset"] = tr_dataset

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/file/{file_id}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponseBody, FileDTO]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = FileDTO.from_dict(response.json())

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
) -> Response[Union[ErrorResponseBody, FileDTO]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    file_id: str,
    *,
    client: AuthenticatedClient,
    tr_dataset: str,
) -> Response[Union[ErrorResponseBody, FileDTO]]:
    """get_file

     get_file

    Download a file from S3 attached to the server based on its id. We plan to add support for getting
    signed S3 URLs to download from S3 directly in a release soon.

    Args:
        file_id (str):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, FileDTO]]
    """

    kwargs = _get_kwargs(
        file_id=file_id,
        tr_dataset=tr_dataset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    file_id: str,
    *,
    client: AuthenticatedClient,
    tr_dataset: str,
) -> Optional[Union[ErrorResponseBody, FileDTO]]:
    """get_file

     get_file

    Download a file from S3 attached to the server based on its id. We plan to add support for getting
    signed S3 URLs to download from S3 directly in a release soon.

    Args:
        file_id (str):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, FileDTO]
    """

    return sync_detailed(
        file_id=file_id,
        client=client,
        tr_dataset=tr_dataset,
    ).parsed


async def asyncio_detailed(
    file_id: str,
    *,
    client: AuthenticatedClient,
    tr_dataset: str,
) -> Response[Union[ErrorResponseBody, FileDTO]]:
    """get_file

     get_file

    Download a file from S3 attached to the server based on its id. We plan to add support for getting
    signed S3 URLs to download from S3 directly in a release soon.

    Args:
        file_id (str):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, FileDTO]]
    """

    kwargs = _get_kwargs(
        file_id=file_id,
        tr_dataset=tr_dataset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    file_id: str,
    *,
    client: AuthenticatedClient,
    tr_dataset: str,
) -> Optional[Union[ErrorResponseBody, FileDTO]]:
    """get_file

     get_file

    Download a file from S3 attached to the server based on its id. We plan to add support for getting
    signed S3 URLs to download from S3 directly in a release soon.

    Args:
        file_id (str):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, FileDTO]
    """

    return (
        await asyncio_detailed(
            file_id=file_id,
            client=client,
            tr_dataset=tr_dataset,
        )
    ).parsed
