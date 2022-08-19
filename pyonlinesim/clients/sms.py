from abc import ABC
from typing import Optional, List

from ..core.abc import BaseAPIClient
from ..core.methods import Methods
from ..types.sms import Balance, NumberStats, OrderNumber, StateInfo, OrderManaged


class OnlineSMS(BaseAPIClient, ABC):
    BASE_URL = 'https://onlinesim.ru/api/'

    def __init__(self, api_key: str):
        super().__init__(api_key)

    async def get_services(self, country: Optional[str] = None) -> NumberStats:
        """
        Get Number Stats
        :param country: Country (If not provided will return all the countries)
        :return: NumberStats
        """
        params = {"country": country}
        result = await self._send_request(Methods.GET_NUMBERS_STATS, params)
        return NumberStats(**result)

    async def order_number(self, service: str, region: Optional[int] = None, country: Optional[int] = None,
                           reject: Optional[List[int]] = None, extension: Optional[int] = None,
                           number: Optional[bool] = None, dev_id: Optional[int] = None) -> OrderNumber:
        """
        Order Number
        :param service: Service ID
        :param region: Region (77 - Moscow for example)
        :param country: Country ID (default=7)
        :param reject: Reject numbers mask ([911, 912] for example)
        :param extension: Extension (default=0)
        :param number: Return Number (default=False)
        :param dev_id: Developer ID
        :return:
        """
        params = {"service": service, "region": region, "country": country, "reject": reject, "extension": extension,
                  "dev_id": dev_id, "number": str(number) if number else None}
        result = await self._send_request(Methods.GET_NUM, params)
        return OrderNumber(**result)

    async def get_order_info(self, operation_id: int, get_full_message: Optional[bool] = False,
                             form: Optional[int] = None, order_by: Optional[str] = None,
                             msg_list: Optional[int] = None, clean: Optional[int] = None) -> StateInfo:
        """
        Get Order Info
        :param clean: Do not show messages on a circle (?).
        :param msg_list: Type of message list, 1 - the list, 0 - the active message
        :param order_by: ascending/descending sorting asc/desc. Default value - asc
        :param form: type of reception, 1 - online reception, 2 - repeated reception, 3 - delayed reception.
        :param get_full_message: Get Full Message. If True, will return the full message.
        :param operation_id: Operation ID
        :return: Order Info
        """
        params = {"tzid": operation_id, "message_to_code": 0 if get_full_message else 1,
                  "form": form, "order_by": order_by, "msg_list": msg_list, "clean": clean}
        result = await self._send_request(Methods.GET_STATE, params)
        corrected_json = {"response": "1", "orders": result}
        return StateInfo(**corrected_json)

    async def finish_order(self, operation_id: int, ban: Optional[bool] = False) -> OrderManaged:
        """
        Finish Order
        :param ban: Block Number (Only for Chinese numbers)
        :param operation_id: Operation ID
        :return: None
        """
        params = {"tzid": operation_id, "ban": 1 if ban else 0}
        result = await self._send_request(Methods.SET_OPERATION_OK, params)
        return OrderManaged(**result)

    async def revise_order(self, operation_id: int) -> OrderManaged:
        """
        Revise Order
        :param operation_id: Operation ID
        :return: None
        """
        params = {"tzid": operation_id}
        result = await self._send_request(Methods.SET_OPERATION_REVISE, params)
        return OrderManaged(**result)
