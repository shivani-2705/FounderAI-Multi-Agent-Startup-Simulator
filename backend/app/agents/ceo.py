from app.agents.base import BaseAgent
from app.agents.schemas import CEOAnalysis


class CEOAgent(BaseAgent):
    @property
    def role(self) -> str:
        return "Chief Executive Officer"

    @property
    def objective(self) -> str:
        return "Analyze startup ideas and define the business vision."

    def system_prompt(self) -> str:
        return """
You are an experienced startup CEO.

Analyze the startup idea.

Return ONLY valid JSON.

Do not include markdown.
Do not include explanations.

Return exactly this schema:

{
    "vision": "...",
    "mission": "...",
    "target_market": "...",
    "target_users": [
        "..."
    ],
    "revenue_model": "...",
    "risks": [
        "..."
    ]
}
"""

    def generate(self, user_prompt: str) -> CEOAnalysis:
        return self.llm.generate_structured(
            system_prompt=self.system_prompt(),
            user_prompt=user_prompt,
            response_model=CEOAnalysis,
        )