from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response_body import ErrorResponseBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    file_id: str,
    *,
    delete_chunks: Union[None, Unset, bool] = UNSET,
    tr_dataset: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["TR-Dataset"] = tr_dataset

    params: Dict[str, Any] = {}

    json_delete_chunks: Union[None, Unset, bool]
    if isinstance(delete_chunks, Unset):
        json_delete_chunks = UNSET
    else:
        json_delete_chunks = delete_chunks
    params["delete_chunks"] = json_delete_chunks

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/api/file/{file_id}",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponseBody]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResponseBody.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ErrorResponseBody]]:
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
    delete_chunks: Union[None, Unset, bool] = UNSET,
    tr_dataset: str,
) -> Response[Union[Any, ErrorResponseBody]]:
    """delete_file

     delete_file

    Delete a file from S3 attached to the server based on its id. This will disassociate chunks from the
    file, but will not delete the chunks. We plan to add support for deleting chunks in a release soon.
    Auth'ed user must be an admin or owner of the dataset's organization to upload a file.

    Args:
        file_id (str):
        delete_chunks (Union[None, Unset, bool]):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponseBody]]
    """

    kwargs = _get_kwargs(
        file_id=file_id,
        delete_chunks=delete_chunks,
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
    delete_chunks: Union[None, Unset, bool] = UNSET,
    tr_dataset: str,
) -> Optional[Union[Any, ErrorResponseBody]]:
    """delete_file

     delete_file

    Delete a file from S3 attached to the server based on its id. This will disassociate chunks from the
    file, but will not delete the chunks. We plan to add support for deleting chunks in a release soon.
    Auth'ed user must be an admin or owner of the dataset's organization to upload a file.

    Args:
        file_id (str):
        delete_chunks (Union[None, Unset, bool]):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponseBody]
    """

    return sync_detailed(
        file_id=file_id,
        client=client,
        delete_chunks=delete_chunks,
        tr_dataset=tr_dataset,
    ).parsed


async def asyncio_detailed(
    file_id: str,
    *,
    client: AuthenticatedClient,
    delete_chunks: Union[None, Unset, bool] = UNSET,
    tr_dataset: str,
) -> Response[Union[Any, ErrorResponseBody]]:
    """delete_file

     delete_file

    Delete a file from S3 attached to the server based on its id. This will disassociate chunks from the
    file, but will not delete the chunks. We plan to add support for deleting chunks in a release soon.
    Auth'ed user must be an admin or owner of the dataset's organization to upload a file.

    Args:
        file_id (str):
        delete_chunks (Union[None, Unset, bool]):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponseBody]]
    """

    kwargs = _get_kwargs(
        file_id=file_id,
        delete_chunks=delete_chunks,
        tr_dataset=tr_dataset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    file_id: str,
    *,
    client: AuthenticatedClient,
    delete_chunks: Union[None, Unset, bool] = UNSET,
    tr_dataset: str,
) -> Optional[Union[Any, ErrorResponseBody]]:
    """delete_file

     delete_file

    Delete a file from S3 attached to the server based on its id. This will disassociate chunks from the
    file, but will not delete the chunks. We plan to add support for deleting chunks in a release soon.
    Auth'ed user must be an admin or owner of the dataset's organization to upload a file.

    Args:
        file_id (str):
        delete_chunks (Union[None, Unset, bool]):
        tr_dataset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponseBody]
    """

    return (
        await asyncio_detailed(
            file_id=file_id,
            client=client,
            delete_chunks=delete_chunks,
            tr_dataset=tr_dataset,
        )
    ).parsed
