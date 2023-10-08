import os

from dotenv import load_dotenv

from pydantic import BaseConfig

load_dotenv()


class APIConfiguration(BaseConfig):
    title: str = os.environ.get("API_TITLE", "FastAPI demo API")
    version: str = os.environ.get("API_VERSION", "0.1.0")
    description: str = os.environ.get("API_DESCRIPTION", "FastAPI demo API")
    docs_url: str = "/docs"
    redoc_url: str = "/redoc"
    openapi_url = "/openapi.json"
    api_prefix: str = os.environ.get("API_PREFIX", "/api")


settings = APIConfiguration()
