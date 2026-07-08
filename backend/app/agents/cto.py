import json

from app.agents.base import BaseAgent
from app.agents.contracts import (
    CEOAnalysis,
    TechnicalArchitecture,
)
from app.utils.prompt_loader import load_prompt

class CTOAgent(BaseAgent):

    @property
    def role(self):
        return "Chief Technology Officer"

    @property
    def objective(self):
        return (
            "Design a scalable technical architecture."
        )

    def system_prompt(self):
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