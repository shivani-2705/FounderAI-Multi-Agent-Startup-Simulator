class LLMError(Exception):
    """Base exception for all LLM-related errors."""


class ModelNotFoundError(LLMError):
    """Raised when the configured model is unavailable."""


class InvalidResponseError(LLMError):
    """Raised when the model returns an unexpected response."""


class LLMConnectionError(LLMError):
    """Raised when Ollama cannot be reached."""