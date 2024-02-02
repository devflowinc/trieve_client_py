from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.default_error import DefaultError
from ...types import Response


def _get_kwargs(
    file_id: str,
    *,
    tr_dataset: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["TR-Dataset"] = tr_dataset

    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/api/file/{file_id}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DefaultError]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
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
    file_id: str,
    *,
    client: AuthenticatedClient,
    tr_dataset: str,
) -> Response[Union[Any, DefaultError]]:
    """delete_file

     delete_file

    Delete a file from S3 attached to the server based on its id. This will disassociate chunks from the
    file, but will not delete the chunks. We plan to add support for deleting chunks in a release soon.
    Auth'ed user must be an admin or owner of the dataset's organization to upload a file.

    Args:
        file_id (str):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DefaultError]]
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
) -> Optional[Union[Any, DefaultError]]:
    """delete_file

     delete_file

    Delete a file from S3 attached to the server based on its id. This will disassociate chunks from the
    file, but will not delete the chunks. We plan to add support for deleting chunks in a release soon.
    Auth'ed user must be an admin or owner of the dataset's organization to upload a file.

    Args:
        file_id (str):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DefaultError]
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
) -> Response[Union[Any, DefaultError]]:
    """delete_file

     delete_file

    Delete a file from S3 attached to the server based on its id. This will disassociate chunks from the
    file, but will not delete the chunks. We plan to add support for deleting chunks in a release soon.
    Auth'ed user must be an admin or owner of the dataset's organization to upload a file.

    Args:
        file_id (str):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DefaultError]]
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
) -> Optional[Union[Any, DefaultError]]:
    """delete_file

     delete_file

    Delete a file from S3 attached to the server based on its id. This will disassociate chunks from the
    file, but will not delete the chunks. We plan to add support for deleting chunks in a release soon.
    Auth'ed user must be an admin or owner of the dataset's organization to upload a file.

    Args:
        file_id (str):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DefaultError]
    """

    return (
        await asyncio_detailed(
            file_id=file_id,
            client=client,
            tr_dataset=tr_dataset,
        )
    ).parsed
