from abc import ABC
from typing import Optional, List

from ..core.abc import BaseAPIClient
from ..core.methods import RentMethods
from ..types.rent import RentTariff


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

    async def rent_number(self, country: int, days: int, extension: Optional[bool] = False,
                          pagination: Optional[bool] = False):
        params = {'country': country, 'days': days, 'extension': extension, 'pagination': pagination}

    @staticmethod
    def _modify_tariffs_json(json: dict) -> RentTariff:
        numbers_json = {"numbers": {}}
        for k, v in json['days'].items():
            numbers_json["numbers"][k] = {'amount': json['count'][k], 'price': json['days'][k]}
        json |= numbers_json
        json.pop('count')
        json.pop('days')
        return RentTariff(**json)
