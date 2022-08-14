import abc
from typing import Optional, Union, List

from pyonlinesim.core.methods import Methods, RentMethods


class BaseAPIClient(abc.ABC):
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def _send_request(self, method: Union[Methods, RentMethods], params: Optional[dict] = None) -> None:
        pass

    async def get_balance(self) -> None:
        pass

    async def get_services(self, country: Optional[str] = None) -> None:
        pass

    async def order_number(self, service: str, region: Optional[int] = None, country: Optional[int] = None,
                           reject: Optional[List[int]] = None, extension: Optional[int] = None,
                           number: Optional[bool] = None, dev_id: Optional[int] = None) -> None:
        pass

    async def get_order_info(self, operation_id: int, get_full_message: Optional[bool] = False,
                             form: Optional[int] = None, order_by: Optional[str] = None,
                             msg_list: Optional[int] = None, clean: Optional[int] = None) -> None:
        pass

    async def finish_order(self, operation_id: int, ban: Optional[bool] = False) -> None:
        pass

    async def revise_order(self, operation_id: int) -> None:
        pass
