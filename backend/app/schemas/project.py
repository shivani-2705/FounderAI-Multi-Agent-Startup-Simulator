from typing import Any
from datetime import datetime
from pydantic import BaseModel

from app.memory.events import EventType


class ProjectCreate(BaseModel):
    name: str
    idea: str


class ProjectCreateResponse(BaseModel):
    project_id: str
    status: str


class ProjectResults(BaseModel):
    ceo_analysis: dict[str, Any] | None = None
    technical_architecture: dict[str, Any] | None = None
    prd: dict[str, Any] | None = None
    design: dict[str, Any] | None = None
    marketing: dict[str, Any] | None = None
    investment: dict[str, Any] | None = None


class ProjectResponse(BaseModel):
    project_id: str
    status: str
    idea: str

    current_agent: str | None = None
    progress: int
    error_message: str | None = None

    results: ProjectResults


class ProjectStatusResponse(BaseModel):
    project_id: str
    status: str
    current_agent: str | None = None
    progress: int


class HistoryEvent(BaseModel):
    timestamp: str
    agent: str
    event_type: str
    message: str

class HistoryEventResponse(BaseModel):
    timestamp: datetime
    agent: str
    event_type: EventType
    content: str


class ProjectHistoryResponse(BaseModel):
    project_id: str
    events: list[HistoryEventResponse]