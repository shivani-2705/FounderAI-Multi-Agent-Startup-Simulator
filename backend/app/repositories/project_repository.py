from sqlalchemy.orm import Session

from app.db.models.project import Project


class ProjectRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        name: str,
        idea: str,
    ) -> Project:

        project = Project(
            name=name,
            idea=idea,
        )

        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)

        return project