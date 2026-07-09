from pydantic import BaseModel, Field

from app.memory.events import AgentEvent


class ConversationHistory(BaseModel):

    events: list[AgentEvent] = Field(
        default_factory=list
    )

    def add(self, event: AgentEvent):

        self.events.append(event)