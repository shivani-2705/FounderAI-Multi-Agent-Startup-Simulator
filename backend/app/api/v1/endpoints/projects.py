from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.api.dependencies import get_db

from app.repositories.project_repository import (
    project_repository,
)


router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)


@router.get("/{project_id}")
def get_project(
    project_id: str,
    db: Session = Depends(get_db),
):

    project = project_repository.get(
        db,
        project_id,
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )

    return project