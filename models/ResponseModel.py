from pydantic import BaseModel
from typing import List


class DNSRecordResponse(BaseModel):
    domain: str
    record_type: str
    records: List[str] | None


class ErrorResponse(BaseModel):
    error: str

