from pydantic import BaseModel


class LLMResponse(BaseModel):
    content: str
    model: str
    total_duration: int | None = None
    prompt_eval_count: int | None = None
    eval_count: int | None = None