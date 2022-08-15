from typing import List, Optional

from pydantic import BaseModel, Field, validator


class NumberData(BaseModel):
    price: int
    amount: int


class Numbers(BaseModel):
    one_day: Optional[NumberData] = Field(None, alias='1')
    three_days: Optional[NumberData] = Field(None, alias='3')
    seven_days: Optional[NumberData] = Field(None, alias='7')
    fifteen_days: Optional[NumberData] = Field(None, alias='15')
    thirty_days: Optional[NumberData] = Field(None, alias='30')

    # @validator('amount', pre=True)
    # def iter_to_lists(cls, v):
    #     print(v)
    #     return [v[key] for key in list(v)]
    #
    # @validator('price', pre=True)
    # def iter_to_list(cls, v):
    #     return [v[key] for key in list(v)]


class RentTariff(BaseModel):
    id: int = Field(..., alias='code')
    is_enabled: bool = Field(..., alias='enabled')
    country_name: str = Field(..., alias='name')
    is_new: bool = Field(..., alias='new')
    position: int
    numbers: Numbers = Field(..., alias='numbers')
    extend_price: int = Field(..., alias='extend')
    confirm: Optional[bool]
