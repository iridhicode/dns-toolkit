from pydantic import BaseModel,validator
from typing import List , Union
from datetime import datetime

class DomainDetails(BaseModel):
    domain: str
    registrar: str | None
    creation_date: Union[ str,datetime,List[datetime]] | str|  None
    expiration_date: Union[ str,datetime,List[datetime]] | str| None
    last_updated: Union[ str,datetime,List[datetime]] | str| None
    dnssec : str | None
    @validator('creation_date', 'expiration_date', 'last_updated', pre=True)
    def process_date(cls, value):
        if isinstance(value, str):
            try:
                return datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                return None
        elif isinstance(value, list) and value:
            return value[0]
        return value