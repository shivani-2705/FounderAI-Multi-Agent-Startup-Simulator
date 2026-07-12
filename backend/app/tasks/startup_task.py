from app.db.session import SessionLocal

from app.repositories.project_repository import (
    project_repository,
)

from app.orchestrator.orchestrator import (
    startup_orchestrator,
)


def run_startup_project(
    project_id: str,
):
    """
    Background task that runs the AI workflow.
    """

    db = SessionLocal()

    try:

        project = project_repository.get(
            db=db,
            project_id=project_id,
        )

        if not project:
            return

        startup_orchestrator.execute(
            db=db,
            project=project,
        )

    finally:
        db.close()