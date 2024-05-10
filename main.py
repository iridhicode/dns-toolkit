from fastapi import FastAPI ,HTTPException
from fastapi.responses import JSONResponse
from routers import dns_details,header_details,ssl_details


app = FastAPI(title="DNS tool kit",
    version="1.0.0",)

app.include_router(dns_details.app)
app.include_router(header_details.app)
app.include_router(ssl_details.app)

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)