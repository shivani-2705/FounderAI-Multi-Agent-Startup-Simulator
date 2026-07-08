from fastapi import APIRouter
from app.workflows.state import StartupState

from app.schemas.startup import StartupRequest
from app.workflows.startup_workflow import startup_workflow
from app.services.ai_services import ai_service

router = APIRouter()


@router.post(
    "/startup/analyze",
    response_model=StartupState,
)
def analyze_startup(
    request: StartupRequest,
):
    return ai_service.analyze_startup(
    request.idea
)