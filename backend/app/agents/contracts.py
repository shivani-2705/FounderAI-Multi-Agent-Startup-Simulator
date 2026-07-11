from pydantic import BaseModel
from enum import Enum


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

class ReviewDecision(str, Enum):
    APPROVED = "approved"
    REVISION_REQUIRED = "revision_required"

class AgentReview(BaseModel):
    decision: ReviewDecision
    feedback: str

class ColorPalette(BaseModel):
    primary: str
    secondary: str
    accent: str
    background: str
    surface: str
    text: str


class Typography(BaseModel):
    font_family: str
    heading_style: str
    body_style: str


class Accessibility(BaseModel):
    language_support: str
    keyboard_navigation: str
    contrast: str


class DesignComponent(BaseModel):
    component: str
    description: str


class DesignDocument(BaseModel):
    design_style: str
    color_palette: ColorPalette
    typography: Typography
    design_principles: list[str]
    key_screens: list[str]
    user_flow: list[str]
    ui_components: list[DesignComponent]
    accessibility: Accessibility


class MarketingStrategy(BaseModel):
    brand_positioning: str
    value_proposition: str
    target_audience: list[str]
    marketing_channels: list[str]
    launch_plan: list[str]
    content_strategy: list[str]
    success_metrics: list[str]

class InvestmentReport(BaseModel):
    investment_score: int
    recommendation: str
    strengths: list[str]
    weaknesses: list[str]
    risks: list[str]
    suggested_valuation: str
    funding_stage: str
    next_steps: list[str]