import json
from typing import Type, TypeVar

from ollama import Client
from pydantic import BaseModel

from app.core.config import settings
from app.core.logging import logger
from app.llm.schemas import LLMResponse

T = TypeVar("T", bound=BaseModel)


class LLMClient:
    def __init__(self):
        self.client = Client(host=settings.ollama_host)

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> LLMResponse:
        logger.info(f"Calling model: {settings.llm_model}")

        response = self.client.chat(
            model=settings.llm_model,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
            options={
                "temperature": settings.llm_temperature,
            },
        )

        return LLMResponse(
            content=response["message"]["content"],
            model=response["model"],
            total_duration=response.get("total_duration"),
            prompt_eval_count=response.get("prompt_eval_count"),
            eval_count=response.get("eval_count"),
        )

    def generate_structured(
        self,
        system_prompt: str,
        user_prompt: str,
        response_model: Type[T],
    ) -> T:
        logger.info(
            f"Calling model (structured): {settings.llm_model}"
        )

        response = self.client.chat(
            model=settings.llm_model,
            format="json",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
            options={
                "temperature": settings.llm_temperature,
            },
        )

        data = json.loads(response["message"]["content"])

        return response_model.model_validate(data)


llm = LLMClient()