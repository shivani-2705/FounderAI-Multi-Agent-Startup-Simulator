from enum import Enum


class LLMModel(str, Enum):
    QWEN_3_8B = "qwen3:8b"
    LLAMA_3_1_8B = "llama3.1:8b"