import json

from app.agents.base import BaseAgent
from app.agents.contracts import (
    CEOAnalysis,
    TechnicalArchitecture,
    PRDDocument,
)
from app.utils.prompt_loader import load_prompt

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
    ) -> PRDDocument:
        # Corrected indentation: 4 spaces inside the method block
        context = {
            "business": ceo_analysis.model_dump(),
            "technology": architecture.model_dump(),
        }

        user_prompt = json.dumps(
            context,
            indent=2,
        )
        
        return self.llm.generate_structured(
            system_prompt=self.system_prompt(),
            user_prompt=user_prompt,
            response_model=PRDDocument,
        )