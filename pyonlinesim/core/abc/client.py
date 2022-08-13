import abc
from typing import Optional, Union

from aiohttp import ClientSession

from pyonlinesim.core.methods import Methods, RentMethods


class BaseAPIClient(abc.ABC):
    def __init__(self, api_key: str, session: Optional[ClientSession] = None):
        self.api_key = api_key
        self._session = session

    @abc.abstractmethod
    async def _send_request(self, method: Union[Methods, RentMethods], params: Optional[dict] = None) -> None:
        pass

    def _get_session(self) -> ClientSession:
        pass
