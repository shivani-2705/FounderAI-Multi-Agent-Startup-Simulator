from app.agents.ceo import CEOAgent
from app.agents.contracts import CEOAnalysis


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

    def run(self, idea: str) -> CEOAnalysis:
        return self.ceo.generate(idea)

startup_workflow = StartupWorkflow()