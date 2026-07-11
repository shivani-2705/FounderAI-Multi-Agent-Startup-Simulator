import json

from app.agents.base import BaseAgent
from app.agents.contracts import (
    CEOAnalysis,
    TechnicalArchitecture,
    PRDDocument,
    AgentReview,
    ReviewDecision,
)
from app.utils.prompt_loader import load_prompt
from app.rag.context_builder import context_builder

from app.memory.events import EventHistory
from app.memory.history_formatter import history_formatter


class PMAgent(BaseAgent):

    @property
    def role(self):
        return "Product Manager"

    @property
    def objective(self):
        return (
            "Create a product requirements document."
        )

    def system_prompt(self):
        return load_prompt("pm")

    def generate(
        self,
        ceo_analysis: CEOAnalysis,
        architecture: TechnicalArchitecture,
        history: EventHistory,
    ) -> PRDDocument:

        ceo_json = json.dumps(
            ceo_analysis.model_dump(),
            indent=2,
        )

        cto_json = json.dumps(
            architecture.model_dump(),
            indent=2,
        )

        knowledge = context_builder.build(
            collection_name="startup",
            query = "\n".join([
                ceo_analysis.vision,
                ceo_analysis.mission,
                ceo_analysis.target_market,
                architecture.architecture_style,
                " ".join(architecture.backend),
            ]),
        )
        
        history_text = history_formatter.format(history)
        prompt = load_prompt("pm_rag")

        prompt = (
            prompt.replace("{{ceo}}", ceo_json)
            .replace("{{cto}}", cto_json)
            .replace("{{history}}", history_text)
            .replace("{{context}}", knowledge)
        )

        return self.llm.generate_structured(
            system_prompt=self.system_prompt(),
            user_prompt=prompt,
            response_model=PRDDocument,
        )

    def review(
        self,
        architecture: TechnicalArchitecture,
    ) -> AgentReview:

        if architecture.architecture_style.lower().startswith("microservices"):

            return AgentReview(
                decision=ReviewDecision.REVISION_REQUIRED,
                feedback=(
                    "The proposed architecture is too complex for an MVP. "
                    "Prefer a modular monolith unless independent scaling is required."
                ),
            )

        return AgentReview(
            decision=ReviewDecision.APPROVED,
            feedback="Architecture is appropriate for the current product scope.",
        )