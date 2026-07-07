import json
from typing import Any, TypeVar

from ollama import Client
from pydantic import BaseModel

from app.core.config import settings
from app.core.logging import logger
from app.llm.exceptions import (
    InvalidResponseError,
    StructuredOutputError,
)
from app.llm.schemas import LLMResponse

T = TypeVar("T", bound=BaseModel)


class LLMClient:
    def __init__(self) -> None:
        self.client = Client(host=settings.ollama_host)

    def _build_messages(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> list[dict[str, str]]:
        return [
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ]

    def _chat(
        self,
        messages: list[dict[str, str]],
        response_format: str | None = None,
    ) -> dict[str, Any]:
        logger.info("Calling model: {}", settings.llm_model)

        return self.client.chat(
            model=settings.llm_model,
            messages=messages,
            format=response_format,
            options={
                "temperature": settings.llm_temperature,
            },
        )

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> LLMResponse:
        messages = self._build_messages(
            system_prompt,
            user_prompt,
        )

        response = self._chat(messages)

        content = response["message"]["content"]

        if not content:
            raise InvalidResponseError(
                "Received an empty response from the model."
            )

        return LLMResponse(
            content=content,
            model=response["model"],
            total_duration=response.get("total_duration"),
            prompt_eval_count=response.get("prompt_eval_count"),
            eval_count=response.get("eval_count"),
        )

    def generate_structured(
        self,
        system_prompt: str,
        user_prompt: str,
        response_model: type[T],
    ) -> T:
        messages = self._build_messages(
            system_prompt,
            user_prompt,
        )

        response = self._chat(
            messages=messages,
            response_format="json",
        )

        content = response["message"]["content"]

        if not content:
            raise InvalidResponseError(
                "Received an empty response from the model."
            )

        try:
            data = json.loads(content)
        except json.JSONDecodeError as exc:
            raise StructuredOutputError(
                "Model returned invalid JSON."
            ) from exc

        return response_model.model_validate(data)


llm = LLMClient()