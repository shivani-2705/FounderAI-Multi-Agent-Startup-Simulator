from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.repositories.project_repository import project_repository
from app.schemas.project import (
    ProjectCreateResponse,
    ProjectHistoryResponse,
    ProjectResponse,
    ProjectResults,
    ProjectStatusResponse,
)
from app.services.project_service import ProjectService

router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)


@router.post(
    "",
    response_model=ProjectCreateResponse,
)
def create_project(
    idea: str,
    db: Session = Depends(get_db),
):
    """
    Create a new startup project.
    """

    service = ProjectService(db)

    project = service.create_project(
        idea=idea,
    )

    return ProjectCreateResponse(
        project_id=project.id,
        status=project.status,
    )


@router.get(
    "/{project_id}",
    response_model=ProjectResponse,
)
def get_project(
    project_id: str,
    db: Session = Depends(get_db),
):

    project = project_repository.get(
        db=db,
        project_id=project_id,
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )

    return ProjectResponse(
    project_id=project.id,
    status=project.status,
    idea=project.idea,
    current_agent=project.current_agent,
    progress=project.progress,
    error_message=project.error_message,
    results=ProjectResults(
        ceo_analysis=project.ceo_analysis,
        technical_architecture=project.technical_architecture,
        prd=project.prd,
        design=project.design,
        marketing=project.marketing,
        investment=project.investment,
    ),
)


@router.get(
    "/{project_id}/status",
    response_model=ProjectStatusResponse,
)
def get_project_status(
    project_id: str,
    db: Session = Depends(get_db),
):
    """
    Lightweight endpoint used by frontend polling.
    """

    project = project_repository.get(
        db=db,
        project_id=project_id,
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )

    return ProjectStatusResponse(
        project_id=project.id,
        status=project.status,
        current_agent=project.current_agent,
        progress=project.progress,
    )


@router.get(
    "/{project_id}/history",
    response_model=ProjectHistoryResponse,
)
def get_project_history(
    project_id: str,
    db: Session = Depends(get_db),
):

    project = project_repository.get(
        db=db,
        project_id=project_id,
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )

    return ProjectHistoryResponse(
        project_id=project.id,
        events=project.history["events"] if project.history else [],
    )