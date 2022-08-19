from abc import ABC
from typing import Optional, List

from ..core.abc import BaseAPIClient
from ..core.methods import RentMethods
from ..types import OrderManaged
from ..types.rent import RentTariff, RentNumber


class OnlineRent(BaseAPIClient, ABC):
    BASE_URL = 'https://onlinesim.ru/api/rent/'

    def __init__(self, api_key: str):
        super().__init__(api_key)

    async def get_tariffs(self, country: Optional[int] = None) -> List[RentTariff]:
        """
        Get rent tariffs
        :param country: Country ID
        :return: List[RentTariff]
        """
        params = {'country': country}
        results = await self._send_request(RentMethods.TARIFFS_RENT, params=params)
        return [self._modify_tariffs_json(v) for v in results.values()]

    async def rent_number(self, country: int, days: int, auto_renewal: Optional[bool] = False,
                          pagination: Optional[bool] = False) -> RentNumber:
        """
        Rent a number
        :param country: Country ID
        :param days: Rent length in days
        :param auto_renewal: Auto-extend the rent
        :param pagination: Paginate messages
        :return: RentNumber
        """
        params = {'country': country, 'days': days, 'extension': str(auto_renewal), 'pagination': str(pagination)}
        result = await self._send_request(RentMethods.GET_RENT_NUM, params=params)
        json_modified = self._modify_rent_json(result['item'])
        return RentNumber(**json_modified)

    async def get_rent_info(self, operation_id: int, pagination: Optional[bool] = False) -> RentNumber:
        """
        Get rent info
        :param operation_id: Operation ID
        :param pagination: Paginate messages
        :return:
        """
        params = {'operation_id': operation_id, 'pagination': str(pagination)}
        result = await self._send_request(RentMethods.GET_RENT_STATE, params=params)
        json_modified = self._modify_rent_json(result['list'][0])
        return RentNumber(**json_modified)

    async def extend_rent(self, operation_id: int, days: int) -> RentNumber:
        """
        Extend number rent
        :param operation_id: Operation ID
        :param days: Extend for days
        :return:
        """
        params = {'operation_id': operation_id, 'days': days}
        result = await self._send_request(RentMethods.EXTEND_RENT_STATE, params=params)
        json_modified = self._modify_rent_json(result['list'][0])
        return RentNumber(**json_modified)

    async def finish_rent(self, operation_id: int) -> OrderManaged:
        """
        Finish rent
        :param operation_id: Operation ID
        :return:
        """
        params = {'operation_id': operation_id}
        result = await self._send_request(RentMethods.CLOSE_RENT_NUM, params=params)
        return OrderManaged(**result)

    @staticmethod
    def _modify_tariffs_json(json: dict) -> RentTariff:
        numbers_json = {"numbers": {}}
        for k, v in json['days'].items():
            numbers_json["numbers"][k] = {'amount': json['count'][k], 'price': json['days'][k]}
        json |= numbers_json
        json.pop('count')
        json.pop('days')
        return RentTariff(**json)

    @staticmethod
    def _modify_rent_json(json: dict):
        new_json = {'time_left': {}}
        new_json['time_left']['days'] = json['days']
        new_json['time_left']['hours'] = json['hours']
        new_json['time_left']['minutes'] = json['time']
        json |= new_json
        json.pop('days')
        json.pop('hours')
        json.pop('time')
        return json
