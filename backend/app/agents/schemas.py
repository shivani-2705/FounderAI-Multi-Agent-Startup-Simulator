from pydantic import BaseModel


class CEOAnalysis(BaseModel):
    vision: str
    mission: str
    target_market: str
    target_users: list[str]
    revenue_model: str
    risks: list[str]