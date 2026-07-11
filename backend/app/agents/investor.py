import json

from app.agents.base import BaseAgent
from app.agents.contracts import (
    CEOAnalysis,
    TechnicalArchitecture,
    PRDDocument,
    DesignDocument,
    MarketingStrategy,
    InvestmentReport,
)

from app.utils.prompt_loader import load_prompt
from app.rag.context_builder import context_builder

from app.memory.events import EventHistory
from app.memory.history_formatter import history_formatter


class InvestorAgent(BaseAgent):

    @property
    def role(self) -> str:
        return "Investor"

    @property
    def objective(self) -> str:
        return "Evaluate the startup for investment."

    def system_prompt(self):
        return load_prompt("investor")

    def generate(
        self,
        ceo: CEOAnalysis,
        cto: TechnicalArchitecture,
        prd: PRDDocument,
        design: DesignDocument,
        marketing: MarketingStrategy,
        history: EventHistory,
    ) -> InvestmentReport:

        ceo_json = json.dumps(ceo.model_dump(), indent=2)
        cto_json = json.dumps(cto.model_dump(), indent=2)
        prd_json = json.dumps(prd.model_dump(), indent=2)
        design_json = json.dumps(design.model_dump(), indent=2)
        marketing_json = json.dumps(marketing.model_dump(), indent=2)

        knowledge = context_builder.build(
            collection_name="investor",
            query=(
                ceo.vision
                + "\n"
                + prd.product_name
            ),
        )

        history_text = history_formatter.format(history)

        prompt = load_prompt("investor_rag")

        prompt = (
            prompt.replace("{{ceo}}", ceo_json)
            .replace("{{cto}}", cto_json)
            .replace("{{prd}}", prd_json)
            .replace("{{design}}", design_json)
            .replace("{{marketing}}", marketing_json)
            .replace("{{history}}", history_text)
            .replace("{{context}}", knowledge)
        )

        return self.llm.generate_structured(
            system_prompt=self.system_prompt(),
            user_prompt=prompt,
            response_model=InvestmentReport,
        )