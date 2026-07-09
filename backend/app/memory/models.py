from datetime import datetime

from pydantic import BaseModel, Field


class MemoryEntry(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    agent: str

    message: str