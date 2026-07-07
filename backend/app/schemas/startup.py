from pydantic import BaseModel, Field


class StartupRequest(BaseModel):
    idea: str = Field(
        ...,
        min_length=20,
        max_length=2000,
    )