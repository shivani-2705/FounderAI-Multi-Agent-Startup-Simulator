from enum import Enum

from pydantic import BaseModel


class AgentStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class AgentExecution(BaseModel):
    agent: str
    status: AgentStatus = AgentStatus.PENDING
    duration_ms: float | None = None
    error: str | None = None