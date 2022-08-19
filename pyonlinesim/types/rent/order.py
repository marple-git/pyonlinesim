from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field, validator


class RentStatus(int, Enum):
    WAITING = 0
    CONFIRMED = 1


class RentMessage(BaseModel):
    id: int
    code: str
    created_at: datetime
    service: str
    text: str


class RentMessages(BaseModel):
    current_page: int
    data: Optional[List[RentMessage]]
    first_page: int = Field(None, alias='from')
    last_page: int
    per_page: int
    pages_amount: int = Field(None, alias='to')
    total_messages: int = Field(None, alias='total')


class ExtendRent(BaseModel):
    one_day: Optional[int] = Field(None, alias='1')
    seven_days: Optional[int] = Field(None, alias='7')
    fifteen_days: Optional[int] = Field(None, alias='15')
    thirty_days: Optional[int] = Field(None, alias='30')


class RentNumber(BaseModel):
    status: RentStatus
    messages: Optional[RentMessages] = Field(None, alias='messages')
    country: int
    rent: int
    extension: int
    checked_time: datetime
    sum: float
    number: str
    operation_id: int = Field(..., alias='tzid')
    extend: Optional[ExtendRent] = Field(None, alias='extend')
    checked: bool
    reload: int
    day_extend: int
    m_ext: bool
    freeze: bool

    @validator('messages', pre=True)
    def validate_messages(cls, v):
        return None if v == [] else RentMessages(**v)

    @validator('extend', pre=True)
    def validate_extend(cls, v):
        return None if v == [] else ExtendRent(**v)
