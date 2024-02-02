from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response_body import ErrorResponseBody
from ...types import Response


def _get_kwargs(
    file_name: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/image/{file_name}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponseBody]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, None)
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
) -> Response[Union[Any, ErrorResponseBody]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    file_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ErrorResponseBody]]:
    """get_image_file

     get_image_file

    We strongly recommend not using this endpoint. It is disabled on the managed version and only meant
    for niche on-prem use cases where an image directory is mounted. Get in touch with us thru
    information on docs.trieve.ai for more information.

    Args:
        file_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponseBody]]
    """

    kwargs = _get_kwargs(
        file_name=file_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    file_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ErrorResponseBody]]:
    """get_image_file

     get_image_file

    We strongly recommend not using this endpoint. It is disabled on the managed version and only meant
    for niche on-prem use cases where an image directory is mounted. Get in touch with us thru
    information on docs.trieve.ai for more information.

    Args:
        file_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponseBody]
    """

    return sync_detailed(
        file_name=file_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    file_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ErrorResponseBody]]:
    """get_image_file

     get_image_file

    We strongly recommend not using this endpoint. It is disabled on the managed version and only meant
    for niche on-prem use cases where an image directory is mounted. Get in touch with us thru
    information on docs.trieve.ai for more information.

    Args:
        file_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponseBody]]
    """

    kwargs = _get_kwargs(
        file_name=file_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    file_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ErrorResponseBody]]:
    """get_image_file

     get_image_file

    We strongly recommend not using this endpoint. It is disabled on the managed version and only meant
    for niche on-prem use cases where an image directory is mounted. Get in touch with us thru
    information on docs.trieve.ai for more information.

    Args:
        file_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponseBody]
    """

    return (
        await asyncio_detailed(
            file_name=file_name,
            client=client,
        )
    ).parsed
