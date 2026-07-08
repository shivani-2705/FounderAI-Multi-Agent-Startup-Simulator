from app.agents.contracts import CEOAnalysis
from app.workflows.startup_workflow import startup_workflow


class AIService:
    """
    Coordinates AI-related business operations.
    """

    def analyze_startup(
        self,
        idea: str,
    ) -> CEOAnalysis:

        return startup_workflow.run(
            idea
        )


ai_service = AIService()