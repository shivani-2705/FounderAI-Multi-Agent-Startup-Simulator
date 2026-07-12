from sqlalchemy.orm import Session

from app.workflows.startup_workflow import startup_workflow
from app.workflows.state import StartupState

from app.agents.contracts import ReviewDecision

from app.db.models.project import Project
from app.repositories.project_repository import project_repository

from app.memory.events import (
    AgentEvent,
    EventType,
)


class StartupOrchestrator:
    """
    Controls the conversation between agents.
    """

    def _update_progress(
        self,
        db: Session,
        project: Project,
        *,
        status: str,
        current_agent: str,
        progress: int,
    ):
        project.status = status
        project.current_agent = current_agent
        project.progress = progress

        project_repository.update(db, project)

    def _add_history(
        self,
        db: Session,
        project: Project,
        *,
        agent: str,
        event_type: EventType,
        content: str,
    ):

        if project.history is None:
            project.history = {"events": []}

        project.history["events"].append(
            AgentEvent(
                agent=agent,
                event_type=event_type,
                content=content,
            ).model_dump(mode="json")
        )

        project_repository.update(db, project)

    def _mark_failed(
        self,
        db: Session,
        project: Project,
        error: Exception,
    ):

        project.status = "failed"
        project.current_agent = "Failed"
        project.error_message = str(error)

        self._add_history(
            db=db,
            project=project,
            agent="System",
            event_type=EventType.DECISION,
            content=f"Workflow failed: {error}",
        )

        project_repository.update(db, project)

    def execute(
        self,
        db: Session,
        project: Project,
    ) -> StartupState:

        state = StartupState(
            idea=project.idea,
        )

        project.error_message = None

        self._add_history(
            db=db,
            project=project,
            agent="System",
            event_type=EventType.DECISION,
            content="Workflow started.",
        )

        try:

            # ====================================================
            # CEO
            # ====================================================

            self._update_progress(
                db=db,
                project=project,
                status="running",
                current_agent="CEO",
                progress=10,
            )

            startup_workflow.run_ceo(state)

            project.ceo_analysis = state.ceo_analysis.model_dump()

            project_repository.update(db, project)

            self._add_history(
                db=db,
                project=project,
                agent="CEO",
                event_type=EventType.ANALYSIS,
                content="Generated startup analysis.",
            )

            # ====================================================
            # CTO
            # ====================================================

            self._update_progress(
                db=db,
                project=project,
                status="running",
                current_agent="CTO",
                progress=25,
            )

            startup_workflow.run_cto(state)

            project.technical_architecture = (
                state.technical_architecture.model_dump()
            )

            project_repository.update(db, project)

            self._add_history(
                db=db,
                project=project,
                agent="CTO",
                event_type=EventType.ANALYSIS,
                content="Generated technical architecture.",
            )

            review = startup_workflow.review_cto(state)

            if review.decision == ReviewDecision.REVISION_REQUIRED:

                self._add_history(
                    db=db,
                    project=project,
                    agent="CTO",
                    event_type=EventType.REVIEW,
                    content=review.feedback,
                )

                startup_workflow.revise_ceo(
                    state,
                    review.feedback,
                )

                project.ceo_analysis = state.ceo_analysis.model_dump()

                project_repository.update(db, project)

                self._add_history(
                    db=db,
                    project=project,
                    agent="CEO",
                    event_type=EventType.REVISION,
                    content="CEO analysis revised.",
                )

                startup_workflow.run_cto(state)

                project.technical_architecture = (
                    state.technical_architecture.model_dump()
                )

                project_repository.update(db, project)

                self._add_history(
                    db=db,
                    project=project,
                    agent="CTO",
                    event_type=EventType.REVISION,
                    content="Architecture regenerated.",
                )

            # ====================================================
            # PM
            # ====================================================

            self._update_progress(
                db=db,
                project=project,
                status="running",
                current_agent="PM",
                progress=45,
            )

            review = startup_workflow.review_pm(state)

            if review.decision == ReviewDecision.REVISION_REQUIRED:

                self._add_history(
                    db=db,
                    project=project,
                    agent="PM",
                    event_type=EventType.REVIEW,
                    content=review.feedback,
                )

                startup_workflow.revise_cto(
                    state,
                    review.feedback,
                )

                project.technical_architecture = (
                    state.technical_architecture.model_dump()
                )

                project_repository.update(db, project)

                self._add_history(
                    db=db,
                    project=project,
                    agent="CTO",
                    event_type=EventType.REVISION,
                    content="Architecture updated after PM review.",
                )

            startup_workflow.run_pm(state)

            project.prd = state.prd.model_dump()

            project_repository.update(db, project)

            self._add_history(
                db=db,
                project=project,
                agent="PM",
                event_type=EventType.ANALYSIS,
                content="Generated PRD.",
            )

            # ====================================================
            # Designer
            # ====================================================

            self._update_progress(
                db=db,
                project=project,
                status="running",
                current_agent="Designer",
                progress=65,
            )

            startup_workflow.run_designer(state)

            project.design = state.design.model_dump()

            project_repository.update(db, project)

            self._add_history(
                db=db,
                project=project,
                agent="Designer",
                event_type=EventType.ANALYSIS,
                content="Generated UI/UX design.",
            )

            # ====================================================
            # Marketing
            # ====================================================

            self._update_progress(
                db=db,
                project=project,
                status="running",
                current_agent="Marketing",
                progress=80,
            )

            startup_workflow.run_marketing(state)

            project.marketing = state.marketing.model_dump()

            project_repository.update(db, project)

            self._add_history(
                db=db,
                project=project,
                agent="Marketing",
                event_type=EventType.ANALYSIS,
                content="Generated go-to-market strategy.",
            )

            # ====================================================
            # Investor
            # ====================================================

            self._update_progress(
                db=db,
                project=project,
                status="running",
                current_agent="Investor",
                progress=95,
            )

            startup_workflow.run_investor(state)

            project.investment = state.investment.model_dump()

            project_repository.update(db, project)

            self._add_history(
                db=db,
                project=project,
                agent="Investor",
                event_type=EventType.ANALYSIS,
                content="Generated investment analysis.",
            )

            # ====================================================
            # Completed
            # ====================================================

            project.error_message = None

            self._update_progress(
                db=db,
                project=project,
                status="completed",
                current_agent="Completed",
                progress=100,
            )

            self._add_history(
                db=db,
                project=project,
                agent="System",
                event_type=EventType.DECISION,
                content="Workflow completed successfully.",
            )

            return state

        except Exception as e:

            self._mark_failed(
                db=db,
                project=project,
                error=e,
            )

            raise


startup_orchestrator = StartupOrchestrator()