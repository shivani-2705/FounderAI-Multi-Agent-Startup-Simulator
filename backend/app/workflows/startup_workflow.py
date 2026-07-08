from app.agents.ceo import CEOAgent
from app.agents.cto import CTOAgent
from app.agents.pm import PMAgent
from app.workflows.state import StartupState


class StartupWorkflow:
    """
    Orchestrates all startup agents.

    Currently:
        Idea -> CEO

    Future:
        Idea -> CEO -> CTO -> PM -> Marketing -> Investor
    """

    def __init__(self):
        self.ceo = CEOAgent()
        self.cto = CTOAgent()
        self.pm = PMAgent()

    def run(self, idea: str) -> StartupState:

        state = StartupState(
            idea=idea,
        )

        state.ceo_analysis = self.ceo.generate(
            state.idea,
        )

        state.technical_architecture = self.cto.generate(
            state.ceo_analysis,
        )

        state.prd = self.pm.generate(
            state.ceo_analysis,
            state.technical_architecture,
        )

        return state

startup_workflow = StartupWorkflow()