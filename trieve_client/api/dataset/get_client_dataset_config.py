from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_dataset_configuration import ClientDatasetConfiguration
from ...models.error_response_body import ErrorResponseBody
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/dataset/envs",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ClientDatasetConfiguration, ErrorResponseBody]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ClientDatasetConfiguration.from_dict(response.json())

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
) -> Response[Union[ClientDatasetConfiguration, ErrorResponseBody]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ClientDatasetConfiguration, ErrorResponseBody]]:
    """get_client_dataset_config

     get_client_dataset_config

    Get the client configuration for a dataset. Will use the TR-D

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientDatasetConfiguration, ErrorResponseBody]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ClientDatasetConfiguration, ErrorResponseBody]]:
    """get_client_dataset_config

     get_client_dataset_config

    Get the client configuration for a dataset. Will use the TR-D

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientDatasetConfiguration, ErrorResponseBody]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ClientDatasetConfiguration, ErrorResponseBody]]:
    """get_client_dataset_config

     get_client_dataset_config

    Get the client configuration for a dataset. Will use the TR-D

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientDatasetConfiguration, ErrorResponseBody]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ClientDatasetConfiguration, ErrorResponseBody]]:
    """get_client_dataset_config

     get_client_dataset_config

    Get the client configuration for a dataset. Will use the TR-D

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientDatasetConfiguration, ErrorResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
