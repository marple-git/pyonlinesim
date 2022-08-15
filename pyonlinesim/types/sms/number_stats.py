from typing import List

from pydantic import BaseModel, validator


class ServiceInfo(BaseModel):
    id: int
    count: int
    popular: bool
    code: int
    price: float
    service: str
    slug: str


class NumberStats(BaseModel):
    name: str
    position: int
    code: int
    other: float
    new: bool
    enabled: bool
    services: List[ServiceInfo]

    @validator('services', pre=True)
    def iter_to_list(cls, v):
        return [v[key] for key in list(v)]
