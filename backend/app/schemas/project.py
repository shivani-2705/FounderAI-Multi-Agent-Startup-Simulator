from pydantic import BaseModel, Field


class ProjectCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=200)
    idea: str = Field(..., min_length=10)


class ProjectResponse(BaseModel):
    id: str
    name: str
    idea: str
    status: str

    model_config = {
        "from_attributes": True
    }