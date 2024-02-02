from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response_body import ErrorResponseBody
from ...models.upload_file_data import UploadFileData
from ...models.upload_file_result import UploadFileResult
from ...types import Response


def _get_kwargs(
    *,
    body: UploadFileData,
    tr_dataset: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["TR-Dataset"] = tr_dataset

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/file",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponseBody, UploadFileResult]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UploadFileResult.from_dict(response.json())

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
) -> Response[Union[ErrorResponseBody, UploadFileResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UploadFileData,
    tr_dataset: str,
) -> Response[Union[ErrorResponseBody, UploadFileResult]]:
    """upload_file

     upload_file

    Upload a file to S3 attached to the server. The file will be converted to HTML with tika and chunked
    algorithmically, images will be OCR'ed with tesseract. The resulting chunks will be indexed and
    searchable. Optionally, you can only upload the file and manually create chunks associated to the
    file after. See docs.trieve.ai and/or contact us for more details and tips. Auth'ed user must be an
    admin or owner of the dataset's organization to upload a file.

    Args:
        tr_dataset (str):
        body (UploadFileData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, UploadFileResult]]
    """

    kwargs = _get_kwargs(
        body=body,
        tr_dataset=tr_dataset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: UploadFileData,
    tr_dataset: str,
) -> Optional[Union[ErrorResponseBody, UploadFileResult]]:
    """upload_file

     upload_file

    Upload a file to S3 attached to the server. The file will be converted to HTML with tika and chunked
    algorithmically, images will be OCR'ed with tesseract. The resulting chunks will be indexed and
    searchable. Optionally, you can only upload the file and manually create chunks associated to the
    file after. See docs.trieve.ai and/or contact us for more details and tips. Auth'ed user must be an
    admin or owner of the dataset's organization to upload a file.

    Args:
        tr_dataset (str):
        body (UploadFileData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, UploadFileResult]
    """

    return sync_detailed(
        client=client,
        body=body,
        tr_dataset=tr_dataset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UploadFileData,
    tr_dataset: str,
) -> Response[Union[ErrorResponseBody, UploadFileResult]]:
    """upload_file

     upload_file

    Upload a file to S3 attached to the server. The file will be converted to HTML with tika and chunked
    algorithmically, images will be OCR'ed with tesseract. The resulting chunks will be indexed and
    searchable. Optionally, you can only upload the file and manually create chunks associated to the
    file after. See docs.trieve.ai and/or contact us for more details and tips. Auth'ed user must be an
    admin or owner of the dataset's organization to upload a file.

    Args:
        tr_dataset (str):
        body (UploadFileData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, UploadFileResult]]
    """

    kwargs = _get_kwargs(
        body=body,
        tr_dataset=tr_dataset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UploadFileData,
    tr_dataset: str,
) -> Optional[Union[ErrorResponseBody, UploadFileResult]]:
    """upload_file

     upload_file

    Upload a file to S3 attached to the server. The file will be converted to HTML with tika and chunked
    algorithmically, images will be OCR'ed with tesseract. The resulting chunks will be indexed and
    searchable. Optionally, you can only upload the file and manually create chunks associated to the
    file after. See docs.trieve.ai and/or contact us for more details and tips. Auth'ed user must be an
    admin or owner of the dataset's organization to upload a file.

    Args:
        tr_dataset (str):
        body (UploadFileData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, UploadFileResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            tr_dataset=tr_dataset,
        )
    ).parsed
