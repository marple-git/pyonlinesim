from typing import List, Optional

from pydantic import BaseModel, Field


class OrderState(BaseModel):
    response: str
    operation_id: int = Field(..., alias='tzid')
    service: str
    number: str
    time_left: int = Field(..., alias='time')
    form: str
    country: int
    sum: Optional[int]
    forward_status: Optional[int]
    forward_number: Optional[str]


class StateInfo(BaseModel):
    response: Optional[str]
    orders: List[OrderState]
