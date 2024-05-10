from fastapi import APIRouter, HTTPException
from utils.get_ssl_details import get_ssl_details


app = APIRouter()

@app.get("/ssl-info",tags = ["Fetch SSL Information"])
async def get_ssl_info(domain: str):
    ssl_info = {}
    ssl_info = get_ssl_details(domain)
    if ssl_info:
        return ssl_info
    else:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve ssl details for {domain}")
