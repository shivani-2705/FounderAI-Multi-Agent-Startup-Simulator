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


class UserPersona(BaseModel):
    name: str
    description: str | None = None
    goals: list[str] = []
    pain_points: list[str] = []

class PRDDocument(BaseModel):
    product_name: str
    problem_statement: str
    solution_summary: str
    core_features: list[str]
    user_personas: list[UserPersona]
    mvp_scope: list[str]
    future_scope: list[str]
    success_metrics: list[str]