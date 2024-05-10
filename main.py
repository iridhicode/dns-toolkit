from fastapi import FastAPI ,HTTPException
from fastapi.responses import JSONResponse
from routers import dns,header,ssl


app = FastAPI(title="DNS tool kit",
    version="1.0.0",)

app.include_router(dns.app)
app.include_router(header.app)
app.include_router(ssl.app)

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)