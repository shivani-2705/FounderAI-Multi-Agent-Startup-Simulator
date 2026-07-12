from sqlalchemy.orm import Session

from app.db.models.project import Project
from app.repositories.project_repository import project_repository


class ProjectService:

    def __init__(self, db: Session):
        self.db = db

    def create_project(
        self,
        idea: str,
    ) -> Project:

        project = Project(
            name="New Startup",
            idea=idea,
            status="pending",
            progress=0,
            current_agent="Waiting",
        )

        return project_repository.create(
            self.db,
            project,
        )