from abc import ABC, abstractmethod

from app.llm.client import llm
from app.llm.schemas import LLMResponse


class BaseAgent(ABC):
    def __init__(self):
        self.llm = llm

    @property
    @abstractmethod
    def role(self) -> str:
        pass

    @property
    @abstractmethod
    def objective(self) -> str:
        pass

    @abstractmethod
    def system_prompt(self) -> str:
        pass

   
    def review(self, *args, **kwargs):
        """
        Review another agent's work.
        """
        raise NotImplementedError(
            f"{self.role} does not support reviews."
        )

    def generate(self, user_prompt: str) -> LLMResponse:
        return self.llm.generate(
            system_prompt=self.system_prompt(),
            user_prompt=user_prompt,
        )