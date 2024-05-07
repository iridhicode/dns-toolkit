from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
from utils.dns_resolver import resolve_dns_records
from utils.get_domain_details import get_domain_details
from models.ResponseModel import DNSRecordResponse, ErrorResponse 
from models.RequestModel import DomainDetails
from models.Enum import DNSRecordType

app = FastAPI()

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )

@app.get("/dns-records", response_model=DNSRecordResponse, responses={404: {"model": ErrorResponse}})
async def get_dns_records(domain: str,
                          record_type: DNSRecordType = Query(DNSRecordType.A, description="DNS record type"),
                          page: int = Query(1, ge=1, description="Page number"),
                          page_size: int = Query(10, ge=1, le=100, description="Number of results per page")):
    try:
        print(f"Request from server: {domain} for record type: {record_type.value}")
        records = await resolve_dns_records(domain, record_type)
        print(f"Response from server: {str(records)}")
        if records:
            start = (page - 1) * page_size
            end = start + page_size
            paginated_records = records[start:end]
            return {"domain": domain, "record_type": record_type.value, "records": paginated_records}
        else:
            return {"domain": domain, "record_type": record_type.value, "records": []}
    except Exception as e:
        print(f"Error occurred while resolving DNS: {str(e)}")
        raise HTTPException(status_code=500, detail="An internal server error occurred")
    


@app.get("/domain-details", response_model=DomainDetails, responses={404: {"model": ErrorResponse}})
async def get_domain_info(domain: str):
    domain_details = get_domain_details(domain)
    if domain_details:
        return domain_details
    else:
        raise HTTPException(status_code=404, detail=f"Failed to retrieve domain details for {domain}")