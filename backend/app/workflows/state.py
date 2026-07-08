from pydantic import BaseModel

from app.agents.contracts import (
    CEOAnalysis,
    TechnicalArchitecture,
    PRDDocument,
)


class StartupState(BaseModel):
    idea: str

    ceo_analysis: CEOAnalysis | None = None

    technical_architecture: TechnicalArchitecture | None = None

    prd: PRDDocument | None = None