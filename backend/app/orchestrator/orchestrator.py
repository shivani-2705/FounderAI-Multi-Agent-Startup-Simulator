from sqlalchemy.orm import Session

from app.workflows.startup_workflow import startup_workflow
from app.workflows.state import StartupState

from app.agents.contracts import ReviewDecision

from app.db.models.project import Project
from app.repositories.project_repository import project_repository


class StartupOrchestrator:
    """
    Controls the conversation between agents.
    """

    def execute(
        self,
        db: Session,
        idea: str,
    ) -> StartupState:

        # -----------------------------------------
        # Create Project
        # -----------------------------------------

        project = Project(
            name="New Startup",
            idea=idea,
            status="running",
        )

        project = project_repository.create(
            db,
            project,
        )

        state = StartupState(
            idea=idea,
        )

        # -----------------------------------------
        # CEO
        # -----------------------------------------

        startup_workflow.run_ceo(state)

        project.ceo_analysis = state.ceo_analysis.model_dump()

        project_repository.update(
            db,
            project,
        )

        # -----------------------------------------
        # CTO
        # -----------------------------------------

        startup_workflow.run_cto(state)

        project.technical_architecture = (
            state.technical_architecture.model_dump()
        )

        project_repository.update(
            db,
            project,
        )

        review = startup_workflow.review_cto(state)

        if review.decision == ReviewDecision.REVISION_REQUIRED:

            startup_workflow.revise_ceo(
                state,
                review.feedback,
            )

            project.ceo_analysis = state.ceo_analysis.model_dump()

            project_repository.update(
                db,
                project,
            )

            # CEO changed, regenerate architecture

            startup_workflow.run_cto(state)

            project.technical_architecture = (
                state.technical_architecture.model_dump()
            )

            project_repository.update(
                db,
                project,
            )

        # -----------------------------------------
        # PM Review
        # -----------------------------------------

        review = startup_workflow.review_pm(state)

        if review.decision == ReviewDecision.REVISION_REQUIRED:

            startup_workflow.revise_cto(
                state,
                review.feedback,
            )

            project.technical_architecture = (
                state.technical_architecture.model_dump()
            )

            project_repository.update(
                db,
                project,
            )

        # -----------------------------------------
        # PM
        # -----------------------------------------

        startup_workflow.run_pm(state)

        project.prd = state.prd.model_dump()

        project_repository.update(
            db,
            project,
        )

        # -----------------------------------------
        # Designer
        # -----------------------------------------

        startup_workflow.run_designer(state)

        project.design = state.design.model_dump()

        project_repository.update(
            db,
            project,
        )

        # -----------------------------------------
        # Marketing
        # -----------------------------------------

        startup_workflow.run_marketing(state)

        project.marketing = state.marketing.model_dump()

        project_repository.update(
            db,
            project,
        )

        # -----------------------------------------
        # Investor
        # -----------------------------------------

        startup_workflow.run_investor(state)

        project.investment = state.investment.model_dump()

        project.status = "completed"

        project_repository.update(
            db,
            project,
        )

        return state


startup_orchestrator = StartupOrchestrator()