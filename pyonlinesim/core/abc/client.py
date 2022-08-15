import abc
from typing import Optional, Union, List

from aiohttp import ClientSession

from ... import exceptions
from ..methods import Methods, RentMethods


class BaseAPIClient(abc.ABC):
    BASE_URL = None

    def __init__(self, api_key: str):
        self.api_key = api_key

    async def _send_request(self, method: Union[Methods, RentMethods], params: Optional[dict] = None) -> dict:
        """
        Send request to the API
        :param method: API Method
        :param params: Parameters
        :return: JSON
        """
        async with ClientSession() as session:
            params = self._delete_none(params or {})
            params['apikey'] = self.api_key
            request_url = self._get_request_url(method)
            response = await session.get(request_url, params=params)
            json = await response.json()
            if isinstance(json, dict):
                if json.get("response", None) and str(json['response']) != '1':
                    exceptions.APIError.detect(json['response'])
                elif json.get('original', None) and json['original']['response'] != '1':
                    exceptions.APIError.detect(json['original']['response'])
            return json

    def _get_request_url(self, method: Union[Methods, RentMethods]) -> str:
        return f'{self.BASE_URL}{method.value}.php'

    def _delete_none(self, _dict: dict) -> dict:
        """Delete None values recursively from all of the dictionaries"""
        for key, value in list(_dict.items()):
            if isinstance(value, dict):
                self._delete_none(value)
            elif value is None:
                del _dict[key]
            elif isinstance(value, list):
                for v_i in value:
                    if isinstance(v_i, dict):
                        self._delete_none(v_i)

        return _dict

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        return None

