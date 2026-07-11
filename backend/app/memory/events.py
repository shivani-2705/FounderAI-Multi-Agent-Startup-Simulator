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


class EventHistory:

    def __init__(self):
        self.events: list[AgentEvent] = []


    def add(
        self,
        event: AgentEvent,
    ):
        self.events.append(event)


    def get_all(
        self,
    ) -> list[AgentEvent]:
        return self.events