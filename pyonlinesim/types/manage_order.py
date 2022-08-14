from pydantic import BaseModel, Field


class OrderManaged(BaseModel):
    response: str
    operation_id: int = Field(..., alias='tzid')
