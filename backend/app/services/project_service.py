from sqlalchemy.orm import Session

from app.repositories.project_repository import ProjectRepository
from app.schemas.project import ProjectCreate


class ProjectService:

    def __init__(self, db: Session):
        self.repository = ProjectRepository(db)

    def create_project(self, data: ProjectCreate):
        return self.repository.create(
            name=data.name,
            idea=data.idea,
        )