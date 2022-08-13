from abc import ABC
from typing import Optional, Union

from aiohttp import ClientSession

from pyonlinesim.core.abc import BaseAPIClient
from pyonlinesim.core.methods import Methods, RentMethods
from pyonlinesim.exceptions import API_EXCEPTIONS, throw_exception
from pyonlinesim.types import Balance


class OnlineSim(BaseAPIClient, ABC):
    BASE_URL = 'https://onlinesim.ru/api/'
    RENT_URL = 'https://onlinesim.ru/api/rent/'

    def __init__(self, api_key: str, session: Optional[ClientSession] = None):
        super().__init__(api_key, session)

    async def _send_request(self, method: Union[Methods, RentMethods], params: Optional[dict] = None) -> dict:
        async with self._get_session() as session:
            if params is None:
                params = {}
            params['apikey'] = self.api_key
            request_url = self._get_request_url(method)
            response = await session.get(request_url, params=params)
            json = await response.json()
            if json['response'] in API_EXCEPTIONS:
                throw_exception(json['response'])
            return json

    async def get_balance(self) -> Balance:
        result = await self._send_request(Methods.GET_BALANCE)
        return Balance(**result)

    def _get_session(self) -> ClientSession:
        if self._session is None:
            self._session = ClientSession()
        return self._session

    async def close_session(self):
        await self._session.close()

    def _get_request_url(self, method: Union[Methods, RentMethods]) -> str:
        url = self.BASE_URL if isinstance(method, Methods) else self.RENT_URL
        url += f'{method.value}.php'
        return url
