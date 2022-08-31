from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class OrderStatus(str, Enum):
    WAITING_FOR_NUMBER = 'TZ_INPOOL'
    WAITING_FOR_ANSWER = 'TZ_NUM_WAIT'
    RECEIVED_ANSWER = 'TZ_NUM_ANSWER'
    ANSWER_NOT_RECEIVED = 'TZ_OVER_EMPTY'
    ORDER_FINISHED = 'TZ_OVER_OK'


class OrderState(BaseModel):
    response: OrderStatus
    operation_id: int = Field(..., alias='tzid')
    service: str
    number: str
    time_left: int = Field(..., alias='time')
    message: str = Field(None, alias='msg')
    form: str
    country: int
    sum: Optional[int]
    forward_status: Optional[int]
    forward_number: Optional[str]


class StateInfo(BaseModel):
    response: Optional[str]
    orders: List[OrderState]
