import json

from app.agents.base import BaseAgent
from app.agents.contracts import (
    AgentReview,
    CEOAnalysis,
    ReviewDecision,
    TechnicalArchitecture,
)
from app.utils.prompt_loader import load_prompt


class CTOAgent(BaseAgent):

    @property
    def role(self) -> str:
        return "Chief Technology Officer"

    @property
    def objective(self) -> str:
        return "Design a scalable technical architecture."

    def system_prompt(self) -> str:
        return load_prompt("cto")

    def generate(
        self,
        ceo_analysis: CEOAnalysis,
    ) -> TechnicalArchitecture:

        user_prompt = json.dumps(
            ceo_analysis.model_dump(),
            indent=2,
        )

        return self.llm.generate_structured(
            system_prompt=self.system_prompt(),
            user_prompt=user_prompt,
            response_model=TechnicalArchitecture,
        )

    def review(
        self,
        architecture: TechnicalArchitecture,
    ) -> AgentReview:

        if architecture.architecture_style.lower() == "microservices":
            return AgentReview(
                decision=ReviewDecision.REVISION_REQUIRED,
                feedback="Consider a modular monolith for the MVP to reduce complexity and infrastructure costs.",
            )

        return AgentReview(
            decision=ReviewDecision.APPROVED,
            feedback="Architecture looks good.",
        )