from pydantic import BaseModel


class CEOAnalysis(BaseModel):
    vision: str
    mission: str
    target_market: str
    target_users: list[str]
    revenue_model: str
    risks: list[str]

class TechnicalArchitecture(BaseModel):
    architecture_style: str
    frontend: list[str]
    backend: list[str]
    database: list[str]
    ai_stack: list[str]
    deployment: list[str]
    risks: list[str]