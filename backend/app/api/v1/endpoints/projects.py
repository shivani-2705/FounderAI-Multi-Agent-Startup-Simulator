from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.schemas.project import (
    ProjectCreate,
    ProjectResponse,
)
from app.services.project_service import ProjectService

router = APIRouter()


@router.post(
    "/projects",
    response_model=ProjectResponse,
    status_code=201,
)
def create_project(
    request: ProjectCreate,
    db: Session = Depends(get_db),
):

    service = ProjectService(db)

    return service.create_project(request)