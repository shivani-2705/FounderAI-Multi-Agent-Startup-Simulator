from fastapi import APIRouter

from app.agents.schemas import CEOAnalysis
from app.schemas.startup import StartupRequest
from app.workflows.startup_workflow import startup_workflow

router = APIRouter()


@router.post(
    "/startup/analyze",
    response_model=CEOAnalysis,
)
def analyze_startup(
    request: StartupRequest,
):
    return startup_workflow.run(
        request.idea
    )