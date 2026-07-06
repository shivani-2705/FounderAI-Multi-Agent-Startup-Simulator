from fastapi import FastAPI

from app.api.v1.router import router
from app.core.config import settings
from app.core.logging import logger

logger.info("Starting FounderAI...")

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.include_router(
    router,
    prefix=settings.api_v1_prefix,
)