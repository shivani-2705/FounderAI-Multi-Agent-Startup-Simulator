from fastapi import APIRouter

from app.api.v1.endpoints import (
    health,
    projects,
    startup,
)

router = APIRouter()

router.include_router(
    health.router,
    tags=["Health"],
)

router.include_router(
    projects.router,
    tags=["Projects"],
)

router.include_router(
    startup.router,
    tags=["Startup"],
)