from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response_body import ErrorResponseBody
from ...models.update_chunk_by_tracking_id_data import UpdateChunkByTrackingIdData
from ...types import Response


def _get_kwargs(
    *,
    body: UpdateChunkByTrackingIdData,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/api/chunk/tracking_id/update",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

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
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateChunkByTrackingIdData,
) -> Response[Union[Any, ErrorResponseBody]]:
    """update_chunk_by_tracking_id

     update_chunk_by_tracking_id

    Update a chunk by tracking_id. This is useful for when you are coordinating with an external system
    and want to use the tracking_id to identify the chunk.

    Args:
        body (UpdateChunkByTrackingIdData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponseBody]]
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
    body: UpdateChunkByTrackingIdData,
) -> Optional[Union[Any, ErrorResponseBody]]:
    """update_chunk_by_tracking_id

     update_chunk_by_tracking_id

    Update a chunk by tracking_id. This is useful for when you are coordinating with an external system
    and want to use the tracking_id to identify the chunk.

    Args:
        body (UpdateChunkByTrackingIdData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponseBody]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateChunkByTrackingIdData,
) -> Response[Union[Any, ErrorResponseBody]]:
    """update_chunk_by_tracking_id

     update_chunk_by_tracking_id

    Update a chunk by tracking_id. This is useful for when you are coordinating with an external system
    and want to use the tracking_id to identify the chunk.

    Args:
        body (UpdateChunkByTrackingIdData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponseBody]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateChunkByTrackingIdData,
) -> Optional[Union[Any, ErrorResponseBody]]:
    """update_chunk_by_tracking_id

     update_chunk_by_tracking_id

    Update a chunk by tracking_id. This is useful for when you are coordinating with an external system
    and want to use the tracking_id to identify the chunk.

    Args:
        body (UpdateChunkByTrackingIdData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
