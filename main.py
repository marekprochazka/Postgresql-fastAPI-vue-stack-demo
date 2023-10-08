from fastapi import FastAPI
from core.config import settings


app = FastAPI(
    title=settings.title,
    version=settings.version,
    description=settings.description,
    openapi_prefix=settings.openapi_prefix,
    docs_url=settings.docs_url,
    openapi_url=settings.openapi_url,
    redoc_url=settings.redoc_url,
)


@app.get("/")
async def root():
    return {"Say": "Hello!"}