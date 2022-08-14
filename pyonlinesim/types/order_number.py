from typing import Optional

from pydantic import BaseModel, Field


class OrderNumber(BaseModel):
    response: str
    operation_id: int = Field(..., alias='tzid')
    number: Optional[str]
    country: Optional[str]
