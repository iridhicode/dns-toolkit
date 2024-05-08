from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
from utils.dns_resolver import resolve_dns_records
from utils.get_domain_details import get_domain_details
from utils.get_ssl_details import get_ssl_details
from utils.get_headers import get_headers
from models.ResponseModel import DNSRecordResponse, ErrorResponse 
from models.RequestModel import DomainDetails
from models.Enum import DNSRecordType


app = FastAPI(title="DNS tool kit",
    version="1.0.0",)

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )

@app.get("/dns-records",tags = ["Fetch DNS Records"], response_model=DNSRecordResponse, responses={404: {"model": ErrorResponse}} )
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
    


@app.get("/domain-details",tags = ["Fetch Domain Details"], response_model=DomainDetails, responses={404: {"model": ErrorResponse}})
async def get_domain_info(domain: str):
    domain_details = get_domain_details(domain)
    if domain_details:
        return domain_details
    else:
        raise HTTPException(status_code=404, detail=f"Failed to retrieve domain details for {domain}")


@app.get("/ssl-info",tags = ["Fetch SSL Information"])
async def get_ssl_info(domain: str):
    ssl_info = {}
    ssl_info = get_ssl_details(domain)
    if ssl_info:
        return ssl_info
    else:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve ssl details for {domain}")

@app.get("/headers",tags = ["Fetch HTTP Headers"])
async def get_headers_info(domain: str):  
    headers_info = {}
    headers_info =  get_headers(domain)
    if headers_info:
        return headers_info
    else:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve headers for {domain}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)