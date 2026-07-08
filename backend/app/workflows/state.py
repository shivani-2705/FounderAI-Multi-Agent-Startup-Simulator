from pydantic import BaseModel

from app.agents.contracts import (
    CEOAnalysis,
    TechnicalArchitecture,
)


class StartupState(BaseModel):
    idea: str

    ceo_analysis: CEOAnalysis | None = None

    technical_architecture: TechnicalArchitecture | None = None