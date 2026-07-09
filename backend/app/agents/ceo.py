from app.agents.base import BaseAgent
from app.agents.contracts import CEOAnalysis
from app.utils.prompt_loader import load_prompt
from app.agents.contracts import (
    AgentReview,
    ReviewDecision,
)
import json

class CEOAgent(BaseAgent):
    @property
    def role(self) -> str:
        return "Chief Executive Officer"

    @property
    def objective(self) -> str:
        return "Analyze startup ideas and define the business vision."

    def system_prompt(self):
        return load_prompt("ceo")

    def generate(self, user_prompt: str) -> CEOAnalysis:
        return self.llm.generate_structured(
            system_prompt=self.system_prompt(),
            user_prompt=user_prompt,
            response_model=CEOAnalysis,
        )
    def review(
        self,
        feedback: str,
    ) -> AgentReview:

        return AgentReview(
            decision=ReviewDecision.REVISION_REQUIRED,
            feedback=feedback,
        )

    def revise(
            self,
            analysis: CEOAnalysis,
            feedback: str,
        ) -> CEOAnalysis:

            prompt = (
                f"""
        Previous analysis:

        {json.dumps(analysis.model_dump(), indent=2)}

        CTO Feedback:

        {feedback}
        """
            )

            return self.llm.generate_structured(
                system_prompt=load_prompt("ceo_revision"),
                user_prompt=prompt,
                response_model=CEOAnalysis,
            )

            