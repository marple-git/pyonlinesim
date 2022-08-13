from typing import List, Optional

from pydantic import Field, BaseModel


class Balance(BaseModel):
    response: str
    balance: float
    frozen_balance: float = Field(..., alias='zbalance')