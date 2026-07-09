from pydantic import BaseModel, Field

from app.agents.contracts import (
    CEOAnalysis,
    TechnicalArchitecture,
    PRDDocument,
)
from app.memory.history import ConversationHistory

class StartupState(BaseModel):
    idea: str

    ceo_analysis: CEOAnalysis | None = None

    technical_architecture: TechnicalArchitecture | None = None

    prd: PRDDocument | None = None

    history: ConversationHistory = Field(
    default_factory=ConversationHistory
)