from app.agents.base import BaseAgent
from app.agents.schemas import CEOAnalysis
from app.utils.prompt_loader import load_prompt

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