from sqlalchemy.orm import Session

from app.db.models.project import Project


class ProjectRepository:

    def create(
        self,
        db: Session,
        project: Project,
    ) -> Project:

        db.add(project)
        db.commit()
        db.refresh(project)
        return project

    def update(
        self,
        db: Session,
        project: Project,
    ) -> Project:

        db.add(project)
        db.commit()
        db.refresh(project)
        return project

    def get(
        self,
        db: Session,
        project_id: str,
    ) -> Project | None:

        return (
            db.query(Project)
            .filter(Project.id == project_id)
            .first()
        )


project_repository = ProjectRepository()