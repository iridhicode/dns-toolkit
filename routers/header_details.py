from fastapi import APIRouter, HTTPException
from utils.get_headers import get_headers


app = APIRouter()

@app.get("/headers",tags = ["Fetch HTTP Headers"])
async def get_headers_info(domain: str):  
    headers_info = {}
    headers_info =  get_headers(domain)
    if headers_info:
        return headers_info
    else:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve headers for {domain}")
