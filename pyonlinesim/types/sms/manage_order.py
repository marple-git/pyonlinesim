from typing import Optional

from pydantic import BaseModel, Field


class OrderManaged(BaseModel):
    response: str
    operation_id: Optional[int] = Field(..., alias='tzid')
