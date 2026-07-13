from fastapi import FastAPI

from app.api.v1.router import router
from app.core.config import settings
from app.core.logging import logger

from fastapi.middleware.cors import CORSMiddleware

logger.info("Starting FounderAI...")

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    router,
    prefix=settings.api_v1_prefix,
)