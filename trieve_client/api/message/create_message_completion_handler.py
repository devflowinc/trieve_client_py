from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_message_data import CreateMessageData
from ...models.error_response_body import ErrorResponseBody
from ...types import Response


def _get_kwargs(
    *,
    body: CreateMessageData,
    tr_dataset: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["TR-Dataset"] = tr_dataset

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/message",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponseBody, str]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = response.text
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
) -> Response[Union[ErrorResponseBody, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateMessageData,
    tr_dataset: str,
) -> Response[Union[ErrorResponseBody, str]]:
    """create_message

     create_message

    Create a message. Messages are attached to topics in order to coordinate memory of gen-AI chat
    sessions. We are considering refactoring this resource of the API soon. Currently, you can only send
    user messages. If the topic is a RAG topic then the response will include Chunks first on the
    stream. The structure will look like `[chunks]||mesage`. See docs.trieve.ai for more information.

    Args:
        tr_dataset (str):
        body (CreateMessageData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, str]]
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
    body: CreateMessageData,
    tr_dataset: str,
) -> Optional[Union[ErrorResponseBody, str]]:
    """create_message

     create_message

    Create a message. Messages are attached to topics in order to coordinate memory of gen-AI chat
    sessions. We are considering refactoring this resource of the API soon. Currently, you can only send
    user messages. If the topic is a RAG topic then the response will include Chunks first on the
    stream. The structure will look like `[chunks]||mesage`. See docs.trieve.ai for more information.

    Args:
        tr_dataset (str):
        body (CreateMessageData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, str]
    """

    return sync_detailed(
        client=client,
        body=body,
        tr_dataset=tr_dataset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateMessageData,
    tr_dataset: str,
) -> Response[Union[ErrorResponseBody, str]]:
    """create_message

     create_message

    Create a message. Messages are attached to topics in order to coordinate memory of gen-AI chat
    sessions. We are considering refactoring this resource of the API soon. Currently, you can only send
    user messages. If the topic is a RAG topic then the response will include Chunks first on the
    stream. The structure will look like `[chunks]||mesage`. See docs.trieve.ai for more information.

    Args:
        tr_dataset (str):
        body (CreateMessageData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, str]]
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
    body: CreateMessageData,
    tr_dataset: str,
) -> Optional[Union[ErrorResponseBody, str]]:
    """create_message

     create_message

    Create a message. Messages are attached to topics in order to coordinate memory of gen-AI chat
    sessions. We are considering refactoring this resource of the API soon. Currently, you can only send
    user messages. If the topic is a RAG topic then the response will include Chunks first on the
    stream. The structure will look like `[chunks]||mesage`. See docs.trieve.ai for more information.

    Args:
        tr_dataset (str):
        body (CreateMessageData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, str]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            tr_dataset=tr_dataset,
        )
    ).parsed
