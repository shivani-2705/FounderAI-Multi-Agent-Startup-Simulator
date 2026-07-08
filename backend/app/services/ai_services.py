from app.agents.contracts import CEOAnalysis
from app.orchestrator.orchestrator import startup_orchestrator


class AIService:
    """
    Coordinates AI-related business operations.
    """

    def analyze_startup(
        self,
        idea: str,
    ) -> CEOAnalysis:

        return startup_orchestrator.execute(idea)


ai_service = AIService()