from app.workflows.startup_workflow import startup_workflow
from app.workflows.state import StartupState


class StartupOrchestrator:
    """
    Controls execution of the startup analysis workflow.
    """

    def execute(self, idea: str) -> StartupState:
        return startup_workflow.run(idea)


startup_orchestrator = StartupOrchestrator()