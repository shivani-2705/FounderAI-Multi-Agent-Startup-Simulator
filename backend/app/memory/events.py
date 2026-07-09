from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class EventType(str, Enum):
    ANALYSIS = "analysis"
    REVIEW = "review"
    QUESTION = "question"
    ANSWER = "answer"
    REVISION = "revision"
    DECISION = "decision"

class AgentEvent(BaseModel):

    timestamp: datetime = Field(
        default_factory=datetime.utcnow
    )

    agent: str

    event_type: EventType

    content: str