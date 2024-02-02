from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_topic_data import CreateTopicData
from ...models.error_response_body import ErrorResponseBody
from ...models.topic import Topic
from ...types import Response


def _get_kwargs(
    *,
    body: CreateTopicData,
    tr_dataset: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["TR-Dataset"] = tr_dataset

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/topic",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponseBody, Topic]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Topic.from_dict(response.json())

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
) -> Response[Union[ErrorResponseBody, Topic]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateTopicData,
    tr_dataset: str,
) -> Response[Union[ErrorResponseBody, Topic]]:
    """create_topic

     create_topic

    Create a new chat topic. Topics are attached to a user and act as a coordinator for memory of gen-AI
    chat sessions. We are considering refactoring this resource of the API soon.

    Args:
        tr_dataset (str):
        body (CreateTopicData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, Topic]]
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
    body: CreateTopicData,
    tr_dataset: str,
) -> Optional[Union[ErrorResponseBody, Topic]]:
    """create_topic

     create_topic

    Create a new chat topic. Topics are attached to a user and act as a coordinator for memory of gen-AI
    chat sessions. We are considering refactoring this resource of the API soon.

    Args:
        tr_dataset (str):
        body (CreateTopicData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, Topic]
    """

    return sync_detailed(
        client=client,
        body=body,
        tr_dataset=tr_dataset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateTopicData,
    tr_dataset: str,
) -> Response[Union[ErrorResponseBody, Topic]]:
    """create_topic

     create_topic

    Create a new chat topic. Topics are attached to a user and act as a coordinator for memory of gen-AI
    chat sessions. We are considering refactoring this resource of the API soon.

    Args:
        tr_dataset (str):
        body (CreateTopicData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseBody, Topic]]
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
    body: CreateTopicData,
    tr_dataset: str,
) -> Optional[Union[ErrorResponseBody, Topic]]:
    """create_topic

     create_topic

    Create a new chat topic. Topics are attached to a user and act as a coordinator for memory of gen-AI
    chat sessions. We are considering refactoring this resource of the API soon.

    Args:
        tr_dataset (str):
        body (CreateTopicData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseBody, Topic]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            tr_dataset=tr_dataset,
        )
    ).parsed
