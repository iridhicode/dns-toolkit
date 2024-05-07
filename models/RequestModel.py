from pydantic import BaseModel,validator
from typing import List 
from datetime import datetime

class DomainDetails(BaseModel):
    domain: str
    registrar: str | None
    creation_date: List[datetime] | None
    expiration_date: List[datetime] | None
    last_updated: List[datetime] | None
    status: List[str] | None
    dnssec : str | None
    @validator('creation_date', 'expiration_date', 'last_updated', pre=True)
    def convert_datetime_list(cls, value):
        if isinstance(value, list) and value:
            return [value[0]]
        return value