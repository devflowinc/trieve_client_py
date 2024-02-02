from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response_body import ErrorResponseBody
from ...models.search_chunk_data import SearchChunkData
from ...models.search_chunk_query_response_body import SearchChunkQueryResponseBody
from ...types import Response


def _get_kwargs(
    *,
    body: SearchChunkData,
    tr_dataset: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["TR-Dataset"] = tr_dataset

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/chunk/search",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponseBody, SearchChunkQueryResponseBody]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SearchChunkQueryResponseBody.from_dict(response.json())

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
) -> Response[Union[ErrorResponseBody, SearchChunkQueryResponseBody]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SearchChunkData,
    tr_dataset: str,
) -> Response[Union[ErrorResponseBody, SearchChunkQueryResponseBody]]:
    """search

     search

    This route provides the primary search functionality for the API. It can be used to search for
    chunks by semantic similarity, full-text similarity, or a combination of both. Results' `chunk_html`
    values will be modified with `<b>` tags for sub-sentence highlighting.

    Args:
        tr_dataset (str):
        body (SearchChunkData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, SearchChunkQueryResponseBody]]
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
    body: SearchChunkData,
    tr_dataset: str,
) -> Optional[Union[ErrorResponseBody, SearchChunkQueryResponseBody]]:
    """search

     search

    This route provides the primary search functionality for the API. It can be used to search for
    chunks by semantic similarity, full-text similarity, or a combination of both. Results' `chunk_html`
    values will be modified with `<b>` tags for sub-sentence highlighting.

    Args:
        tr_dataset (str):
        body (SearchChunkData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, SearchChunkQueryResponseBody]
    """

    return sync_detailed(
        client=client,
        body=body,
        tr_dataset=tr_dataset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SearchChunkData,
    tr_dataset: str,
) -> Response[Union[ErrorResponseBody, SearchChunkQueryResponseBody]]:
    """search

     search

    This route provides the primary search functionality for the API. It can be used to search for
    chunks by semantic similarity, full-text similarity, or a combination of both. Results' `chunk_html`
    values will be modified with `<b>` tags for sub-sentence highlighting.

    Args:
        tr_dataset (str):
        body (SearchChunkData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, SearchChunkQueryResponseBody]]
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
    body: SearchChunkData,
    tr_dataset: str,
) -> Optional[Union[ErrorResponseBody, SearchChunkQueryResponseBody]]:
    """search

     search

    This route provides the primary search functionality for the API. It can be used to search for
    chunks by semantic similarity, full-text similarity, or a combination of both. Results' `chunk_html`
    values will be modified with `<b>` tags for sub-sentence highlighting.

    Args:
        tr_dataset (str):
        body (SearchChunkData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, SearchChunkQueryResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            tr_dataset=tr_dataset,
        )
    ).parsed
