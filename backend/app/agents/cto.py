import json

from app.agents.base import BaseAgent
from app.agents.contracts import (
    AgentReview,
    CEOAnalysis,
    ReviewDecision,
    TechnicalArchitecture,
)
from app.utils.prompt_loader import load_prompt
from app.rag.context_builder import context_builder

from app.memory.events import EventHistory
from app.memory.history_formatter import history_formatter


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
        history: EventHistory,
    ) -> TechnicalArchitecture:

        vision = json.dumps(
            ceo_analysis.model_dump(),
            indent=2,
        )

        knowledge = context_builder.build(
            collection_name="startup",
            query = "\n".join([
                ceo_analysis.vision,
                ceo_analysis.mission,
                ceo_analysis.target_market,
                ceo_analysis.revenue_model,
            ]),
        )

        history_text = history_formatter.format(history)


        prompt = load_prompt("cto_rag")

        prompt = (
            prompt.replace(
                "{{vision}}",
                vision,
            ).replace(
                "{{history}}", history_text)
            .replace(
                "{{context}}",
                knowledge,
            )
        )

        return self.llm.generate_structured(
            system_prompt=self.system_prompt(),
            user_prompt=prompt,
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

    def revise(
        self,
        architecture: TechnicalArchitecture,
        feedback: str,
    ) -> TechnicalArchitecture:

        prompt = f"""
    Previous architecture:

    {json.dumps(architecture.model_dump(), indent=2)}

    Feedback:

    {feedback}

    Revise the architecture while keeping the business goals intact.
    """

        return self.llm.generate_structured(
            system_prompt=load_prompt("cto_revision"),
            user_prompt=prompt,
            response_model=TechnicalArchitecture,
        )