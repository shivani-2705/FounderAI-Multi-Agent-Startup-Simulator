from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.api.dependencies import get_db

from app.orchestrator.orchestrator import (
    startup_orchestrator,
)


router = APIRouter(
    prefix="/startup",
    tags=["Startup"],
)


@router.post("/run")
def run_startup(
    idea: str,
    db: Session = Depends(get_db),
):

    result = startup_orchestrator.execute(
        db=db,
        idea=idea,
    )

    return {
        "message": "Startup analysis completed",
        "data": result,
    }