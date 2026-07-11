import json

from app.agents.base import BaseAgent
from app.agents.contracts import (
    CEOAnalysis,
    PRDDocument,
    DesignDocument,
    MarketingStrategy,
)

from app.utils.prompt_loader import load_prompt
from app.rag.context_builder import context_builder

from app.memory.events import EventHistory
from app.memory.history_formatter import history_formatter


class MarketingAgent(BaseAgent):

    @property
    def role(self) -> str:
        return "Marketing Director"

    @property
    def objective(self) -> str:
        return "Create a Go-To-Market strategy."

    def system_prompt(self):
        return load_prompt("marketing")

    def generate(
        self,
        ceo: CEOAnalysis,
        prd: PRDDocument,
        design: DesignDocument,
        history: EventHistory,
    ) -> MarketingStrategy:

        ceo_json = json.dumps(ceo.model_dump(), indent=2)
        prd_json = json.dumps(prd.model_dump(), indent=2)
        design_json = json.dumps(design.model_dump(), indent=2)

        knowledge = context_builder.build(
            collection_name="marketing",
            query=(
                ceo.vision
                + "\n"
                + prd.product_name
            ),
        )

        history_text = history_formatter.format(history)

        prompt = load_prompt("marketing_rag")

        prompt = (
            prompt.replace("{{ceo}}", ceo_json)
            .replace("{{prd}}", prd_json)
            .replace("{{design}}", design_json)
            .replace("{{history}}", history_text)
            .replace("{{context}}", knowledge)
        )

        return self.llm.generate_structured(
            system_prompt=self.system_prompt(),
            user_prompt=prompt,
            response_model=MarketingStrategy,
        )