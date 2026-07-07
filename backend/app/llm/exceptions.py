class LLMError(Exception):
    """Base exception."""


class LLMConnectionError(LLMError):
    """Cannot connect to provider."""


class ModelNotFoundError(LLMError):
    """Configured model not found."""


class InvalidResponseError(LLMError):
    """Invalid LLM response."""


class StructuredOutputError(LLMError):
    """Cannot parse structured output."""