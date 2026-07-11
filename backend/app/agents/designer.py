import json

from app.agents.base import BaseAgent
from app.agents.contracts import (
    CEOAnalysis,
    TechnicalArchitecture,
    PRDDocument,
    DesignDocument,
)

from app.utils.prompt_loader import load_prompt

from app.rag.context_builder import context_builder

from app.memory.events import EventHistory
from app.memory.history_formatter import history_formatter


class DesignerAgent(BaseAgent):

    @property
    def role(self) -> str:
        return "Product Designer"

    @property
    def objective(self) -> str:
        return "Create a complete UI/UX design specification."

    def system_prompt(self) -> str:
        return load_prompt("designer")

    def generate(
        self,
        ceo_analysis: CEOAnalysis,
        architecture: TechnicalArchitecture,
        prd: PRDDocument,
        history: EventHistory,
    ) -> DesignDocument:

        ceo_json = json.dumps(
            ceo_analysis.model_dump(),
            indent=2,
        )

        cto_json = json.dumps(
            architecture.model_dump(),
            indent=2,
        )

        prd_json = json.dumps(
            prd.model_dump(),
            indent=2,
        )

        knowledge = context_builder.build(
            collection_name="design",
            query=(
                ceo_analysis.vision
                + "\n"
                + prd.product_name
                + "\n"
                + architecture.architecture_style
            ),
        )

        history_text = history_formatter.format(history)

        prompt = load_prompt("designer_rag")

        prompt = (
            prompt.replace("{{ceo}}", ceo_json)
            .replace("{{cto}}", cto_json)
            .replace("{{prd}}", prd_json)
            .replace("{{history}}", history_text)
            .replace("{{context}}", knowledge)
        )

        return self.llm.generate_structured(
            system_prompt=self.system_prompt(),
            user_prompt=prompt,
            response_model=DesignDocument,
        )